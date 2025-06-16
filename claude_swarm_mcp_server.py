#!/usr/bin/env python3
"""
True Claude Swarm MCP Server
Actually uses the Claude Swarm framework for agent coordination
"""

import asyncio
import json
import sys
from pathlib import Path

# MCP imports
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Import our Claude Swarm framework
from claude_swarm import ClaudeSwarm, ClaudeAgent, ClaudeResponse

# Storage setup
STORAGE_DIR = Path("/Users/mayank/claude_swarm_agents_mcp/data")
STORAGE_DIR.mkdir(parents=True, exist_ok=True)
AGENTS_FILE = STORAGE_DIR / "agents.json"

# Global state
swarm_client = ClaudeSwarm()
agents = {}  # name -> ClaudeAgent
conversation_history = []
current_agent = None
context_variables = {}

def load_agents():
    global agents, current_agent
    try:
        if AGENTS_FILE.exists():
            with open(AGENTS_FILE, 'r') as f:
                agent_data = json.load(f)
            
            # Recreate ClaudeAgent objects with transfer functions
            for name, data in agent_data.items():
                agent = ClaudeAgent(
                    name=data["name"],
                    model=data["model"],
                    instructions=data["instructions"],
                    functions=[]  # Will add transfer functions below
                )
                agents[name] = agent
            
            # Add transfer functions between agents
            _setup_transfer_functions()
            
            if agents and not current_agent:
                current_agent = list(agents.keys())[0]
                
        print(f"✓ Loaded {len(agents)} Swarm agents", file=sys.stderr)
    except Exception as e:
        print(f"✗ Load error: {e}", file=sys.stderr)

def save_agents():
    """Save agent definitions (functions can't be serialized)"""
    try:
        agent_data = {}
        for name, agent in agents.items():
            agent_data[name] = {
                "name": agent.name,
                "model": agent.model,
                "instructions": agent.instructions
            }
        
        with open(AGENTS_FILE, 'w') as f:
            json.dump(agent_data, f, indent=2)
        print(f"✓ Saved {len(agents)} Swarm agents", file=sys.stderr)
    except Exception as e:
        print(f"✗ Save error: {e}", file=sys.stderr)

def _setup_transfer_functions():
    """Create transfer functions between agents for true Swarm behavior"""
    # Create transfer functions for each agent pair
    transfer_functions = {}
    
    for target_name, target_agent in agents.items():
        def create_transfer(target):
            def transfer_function():
                f"""Transfer to {target.name} for specialized analysis"""
                return target
            transfer_function.__name__ = f"transfer_to_{target.name.lower().replace(' ', '_')}"
            transfer_function.__doc__ = f"Transfer to {target.name} for their specialized expertise"
            return transfer_function
        
        transfer_functions[target_name] = create_transfer(target_agent)
    
    # Add transfer functions to each agent (except self-transfers)
    for source_name, source_agent in agents.items():
        source_agent.functions = []
        for target_name, transfer_func in transfer_functions.items():
            if target_name != source_name:  # Don't transfer to self
                source_agent.functions.append(transfer_func)
    
    print(f"✓ Setup transfer functions for {len(agents)} agents", file=sys.stderr)

async def create_agent_handler(args):
    """Create agent with Swarm integration"""
    name = args.get("name", "")
    instructions = args.get("instructions", "")
    model = args.get("model", "claude-3-5-sonnet-20241022")
    
    if not name or not instructions:
        return "❌ Name and instructions required"
    
    if name in agents:
        return f"❌ Agent '{name}' already exists"
    
    # Create ClaudeAgent object
    agent = ClaudeAgent(
        name=name,
        model=model,
        instructions=instructions,
        functions=[]
    )
    
    agents[name] = agent
    
    # Rebuild transfer functions for all agents
    _setup_transfer_functions()
    
    # Set as current agent if first one
    global current_agent
    if not current_agent:
        current_agent = name
    
    save_agents()
    print(f"✓ Created Swarm agent: {name}", file=sys.stderr)
    return f"✅ Created Swarm agent '{name}' with transfer capabilities!"

async def chat_with_swarm_handler(args):
    """Chat using actual Swarm framework with agent coordination"""
    global conversation_history, current_agent, context_variables
    
    message = args.get("message", "")
    starting_agent_name = args.get("agent_name", current_agent)
    
    if not message:
        return "❌ Message is required"
    
    if not agents:
        return "❌ No agents available. Create agents first."
    
    # Get starting agent
    if starting_agent_name and starting_agent_name in agents:
        starting_agent = agents[starting_agent_name]
    else:
        starting_agent_name = list(agents.keys())[0]
        starting_agent = agents[starting_agent_name]
    
    # Add user message to conversation history
    user_message = {"role": "user", "content": message}
    conversation_history.append(user_message)
    
    try:
        # Use actual Claude Swarm framework
        response = swarm_client.run(
            agent=starting_agent,
            messages=conversation_history,
            context_variables=context_variables,
            debug=True  # Show agent transfers
        )
        
        # Update global state
        conversation_history = response.messages
        current_agent = response.agent.name
        context_variables.update(response.context_variables)
        
        # Get the final response
        last_message = response.messages[-1] if response.messages else {}
        agent_response = last_message.get("content", "No response")
        
        # Check if agent transfer occurred
        transfer_info = ""
        if response.agent.name != starting_agent_name:
            transfer_info = f"\n\n🔄 **Agent Transfer**: {starting_agent_name} → {response.agent.name}"
        
        print(f"✓ Swarm conversation completed: {starting_agent_name} → {response.agent.name}", file=sys.stderr)
        
        return f"🤖 **{response.agent.name}**:\n\n{agent_response}{transfer_info}"
        
    except Exception as e:
        error_msg = f"❌ Swarm error: {str(e)}"
        print(error_msg, file=sys.stderr)
        return error_msg

async def create_finance_team_handler(args):
    """Create finance team with Swarm coordination"""
    company_name = args.get("company_name", "Investment Firm")
    
    team_specs = {
        "Risk_Analyst": {
            "instructions": f"You are a quantitative risk analyst for {company_name}. When users ask about portfolio optimization or investment strategies, transfer to the Portfolio Manager. For market research questions, transfer to the Research Analyst. You specialize in VaR, stress testing, and risk metrics.",
            "model": "claude-3-5-sonnet-20241022"
        },
        "Portfolio_Manager": {
            "instructions": f"You are a portfolio manager for {company_name}. When users ask about risk calculations, transfer to the Risk Analyst. For market analysis, transfer to the Research Analyst. For data questions, transfer to the Data Analyst. You specialize in optimization and asset allocation.",
            "model": "claude-3-5-sonnet-20241022"
        },
        "Data_Analyst": {
            "instructions": f"You are a financial data analyst for {company_name}. When users ask about risk assessment, transfer to the Risk Analyst. For investment advice, transfer to the Portfolio Manager. You specialize in data collection and analysis.",
            "model": "claude-3-5-sonnet-20241022"
        },
        "Research_Analyst": {
            "instructions": f"You are a research analyst for {company_name}. When users ask about portfolio optimization, transfer to the Portfolio Manager. For risk questions, transfer to the Risk Analyst. You specialize in market research and investment analysis.",
            "model": "claude-3-5-sonnet-20241022"
        }
    }
    
    created_agents = []
    for name, specs in team_specs.items():
        if name not in agents:
            # Create ClaudeAgent object
            agent = ClaudeAgent(
                name=name,
                model=specs["model"],
                instructions=specs["instructions"],
                functions=[]
            )
            agents[name] = agent
            created_agents.append(name)
    
    if created_agents:
        # Setup transfer functions for true Swarm behavior
        _setup_transfer_functions()
        
        global current_agent
        current_agent = "Risk_Analyst"
        save_agents()
        
        print(f"✓ Created Swarm finance team: {created_agents}", file=sys.stderr)
    
    result = f"✅ **Swarm Finance Team for {company_name}**\n\n"
    
    if created_agents:
        result += f"**Created agents with transfer capabilities:** {', '.join(created_agents)}\n\n"
        result += "🔄 **Swarm Features Enabled:**\n"
        result += "• Automatic agent handoffs based on expertise\n"
        result += "• Shared conversation context\n"
        result += "• Intelligent routing between specialists\n\n"
        result += "💡 **Try multi-step queries** - agents will coordinate automatically!"
    else:
        result += f"**Team already exists for {company_name}**"
    
    return result

async def get_conversation_history_handler(args):
    """Get the current Swarm conversation state"""
    global conversation_history, current_agent, context_variables
    
    if not conversation_history:
        return "📝 No conversation history yet. Start chatting to see Swarm coordination!"
    
    result = f"🔄 **Swarm Conversation State**\n\n"
    result += f"**Current Agent**: {current_agent}\n"
    result += f"**Context Variables**: {context_variables}\n"
    result += f"**Message Count**: {len(conversation_history)}\n\n"
    
    result += "**Recent Messages**:\n"
    for i, msg in enumerate(conversation_history[-5:], 1):
        role = msg.get("role", "unknown").title()
        content = msg.get("content", "")[:100]
        result += f"{i}. **{role}**: {content}...\n"
    
    return result

def create_server():
    """Create MCP server with true Swarm integration"""
    server = Server("claude-swarm")
    
    @server.list_tools()
    async def list_tools():
        return [
            {
                "name": "create_agent",
                "description": "Create a new Swarm agent with transfer capabilities",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Agent name"},
                        "instructions": {"type": "string", "description": "Agent instructions (include transfer conditions)"},
                        "model": {"type": "string", "default": "claude-3-5-sonnet-20241022"}
                    },
                    "required": ["name", "instructions"]
                }
            },
            {
                "name": "chat_with_swarm",
                "description": "Chat using Claude Swarm with automatic agent coordination",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "message": {"type": "string", "description": "Your message"},
                        "agent_name": {"type": "string", "description": "Starting agent (optional)"}
                    },
                    "required": ["message"]
                }
            },
            {
                "name": "create_finance_team",
                "description": "Create coordinated finance team with Swarm handoffs",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "company_name": {"type": "string", "default": "Investment Firm"}
                    }
                }
            },
            {
                "name": "get_conversation_history",
                "description": "View Swarm conversation state and agent transfers",
                "inputSchema": {"type": "object", "properties": {}}
            },
            {
                "name": "list_agents",
                "description": "List all Swarm agents and their transfer functions",
                "inputSchema": {"type": "object", "properties": {}}
            }
        ]
    
    @server.call_tool()
    async def call_tool(name: str, arguments: dict):
        try:
            if name == "create_agent":
                result = await create_agent_handler(arguments)
            elif name == "chat_with_swarm":
                result = await chat_with_swarm_handler(arguments)
            elif name == "create_finance_team":
                result = await create_finance_team_handler(arguments)
            elif name == "get_conversation_history":
                result = await get_conversation_history_handler(arguments)
            elif name == "list_agents":
                if not agents:
                    result = "📝 No Swarm agents found."
                else:
                    result = f"🔄 **Swarm Agents** ({len(agents)} total):\n\n"
                    for name, agent in agents.items():
                        transfer_count = len(agent.functions)
                        current_marker = "▶️" if name == current_agent else "🤖"
                        result += f"{current_marker} **{name}** ({transfer_count} transfer functions)\n"
                        result += f"   Instructions: {agent.instructions[:80]}...\n\n"
            else:
                result = f"❌ Unknown tool: {name}"
            
            return [{"type": "text", "text": result}]
            
        except Exception as e:
            error_msg = f"❌ Error in {name}: {str(e)}"
            print(error_msg, file=sys.stderr)
            return [{"type": "text", "text": error_msg}]
    
    return server

async def main():
    """Main entry point"""
    print("=== True Claude Swarm MCP Server ===", file=sys.stderr)
    
    # Load existing Swarm agents
    load_agents()
    
    # Create server
    server = create_server()
    print("✓ Swarm server created", file=sys.stderr)
    
    try:
        async with stdio_server() as (read_stream, write_stream):
            print("✓ Connected to Claude Desktop with Swarm coordination", file=sys.stderr)
            
            # Import and setup initialization
            from mcp.server.models import InitializationOptions
            from mcp.server import NotificationOptions
            
            init_options = InitializationOptions(
                server_name="claude-swarm",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            )
            
            await server.run(read_stream, write_stream, init_options)
            
    except Exception as e:
        print(f"✗ Server error: {e}", file=sys.stderr)

if __name__ == "__main__":
    asyncio.run(main())
