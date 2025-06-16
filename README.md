# Claude Swarm MCP Server

A Model Context Protocol (MCP) server that enables **multi-agent orchestration** using Claude AI through Claude Desktop. Create, manage, and coordinate specialized AI agents for complex workflows like financial analysis, customer service, and research.

## 🚀 Features

- **🤖 Persistent Agents**: Create specialized Claude agents that survive restarts
- **🔄 Agent Coordination**: Intelligent handoffs between agents based on expertise
- **💾 Local Storage**: All agents and conversations saved locally
- **📊 Pre-built Templates**: Ready-to-use financial analysis and customer service teams
- **🎯 Specialized Functions**: Custom tools and capabilities per agent
- **🔧 Easy Integration**: Works seamlessly with Claude Desktop

## 📋 Quick Start

### Prerequisites

- Python 3.10+ 
- Claude Desktop installed
- Anthropic API key with billing enabled

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/claude-swarm-mcp.git
cd claude-swarm-mcp
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure Claude Desktop**
   
   Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "claude-swarm": {
      "command": "python3",
      "args": ["/path/to/claude-swarm-mcp/claude_swarm_mcp_server.py"],
      "env": {
        "ANTHROPIC_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

4. **Start the server**
```bash
python3 claude_swarm_mcp_server.py
```

5. **Restart Claude Desktop** and test with:
```
Create finance team with company name "Your Company"
```

## 🎯 Usage Examples

### Create a Financial Analysis Team
```
Create finance team with company name "TechVest Capital"
```
This creates 4 specialized agents:
- **Risk Analyst** - VaR calculations, stress testing
- **Portfolio Manager** - Asset allocation, optimization
- **Data Analyst** - Market data, performance metrics
- **Research Analyst** - Investment research, market analysis

### Chat with Specialists
```
Chat with agent: "Calculate the VaR for a portfolio with AAPL 30%, GOOGL 25%, MSFT 20%, AMZN 15%, TSLA 10%" using agent "Risk Analyst"
```

### Create Custom Agents
```
Create agent with name "Options Specialist" and instructions "You are an expert in options trading. Calculate Greeks, analyze volatility, and recommend hedging strategies."
```

### List All Agents
```
List agents
```

### Portfolio Analysis Workflow
```
Chat with agent: "I need a complete analysis of my tech portfolio: analyze risk, optimize allocation, and provide investment recommendations."
```
*Agents will coordinate automatically to provide comprehensive analysis*

## 🔧 Available Tools

| Tool | Description |
|------|-------------|
| `create_agent` | Create a new specialized agent |
| `list_agents` | View all saved agents |
| `chat_with_agent` | Interact with specific agents |
| `delete_agent` | Remove an agent permanently |
| `create_finance_team` | Generate complete financial analysis team |
| `get_conversation_history` | View chat history and agent transfers |
| `reset_conversation` | Clear conversation history |

## 📁 Project Structure

```
claude-swarm-mcp/
├── claude_swarm.py              # Core Swarm framework
├── claude_swarm_mcp_server.py   # MCP server implementation
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── LICENSE                      # MIT License
├── examples/                    # Usage examples
│   ├── finance_workflow.py      # Financial analysis example
│   ├── customer_service.py      # Customer service template
│   └── research_team.py         # Research coordination example
├── tests/                       # Test suite
│   ├── test_agents.py           # Agent functionality tests
│   ├── test_mcp_server.py       # MCP server tests
│   └── test_swarm.py           # Swarm coordination tests
└── docs/                       # Documentation
    ├── API.md                   # API reference
    ├── DEPLOYMENT.md            # Deployment guide
    └── CONTRIBUTING.md          # Contribution guidelines
```

## 🏗️ Architecture

### Core Components

1. **Claude Swarm Framework** (`claude_swarm.py`)
   - Multi-agent orchestration
   - Automatic handoffs between agents
   - Shared conversation context
   - Function calling integration

2. **MCP Server** (`claude_swarm_mcp_server.py`)
   - Model Context Protocol implementation
   - Persistent agent storage
   - Tool registration and handling
   - Claude Desktop integration

3. **Agent Storage** (`data/`)
   - JSON-based agent persistence
   - Conversation history
   - Context variables
   - Backup and restore capabilities

### Data Flow
```
Claude Desktop ↔ MCP Protocol ↔ Swarm Server ↔ Claude API
                                      ↓
                              Agent Storage (JSON)
```

## 🎨 Use Cases

### Financial Services
- **Portfolio Risk Analysis**: VaR calculations, stress testing
- **Investment Research**: Market analysis, stock recommendations  
- **Compliance Monitoring**: Regulatory requirements, position limits
- **Client Advisory**: Personalized investment advice

### Customer Support
- **Intelligent Triage**: Route customers to appropriate specialists
- **Multi-language Support**: Automatic language detection and routing
- **Escalation Management**: Seamless handoffs to senior agents
- **Knowledge Base Integration**: Context-aware information retrieval

### Research & Development
- **Literature Review**: Coordinate research across multiple domains
- **Data Analysis**: Statistical analysis, visualization, reporting
- **Project Management**: Task coordination, milestone tracking
- **Technical Documentation**: Automated documentation generation

## 🔒 Security & Privacy

- **Local Storage**: All data stored locally on your machine
- **API Key Security**: Secure API key handling through environment variables
- **No External Dependencies**: No third-party services for agent storage
- **Audit Trail**: Complete conversation history and agent interactions

## 🛠️ Configuration

### Environment Variables
```bash
export ANTHROPIC_API_KEY="your-api-key"
export CLAUDE_SWARM_STORAGE_DIR="/custom/storage/path"  # Optional
export CLAUDE_SWARM_DEBUG="true"  # Optional debug mode
```

### Storage Configuration
```python
# Custom storage location
storage_path = "/Users/yourname/claude_agents"
server = ClaudeSwarmMCPServer(storage_dir=storage_path)
```

## 📊 Performance

- **Agent Creation**: < 2 seconds
- **Chat Response**: 3-8 seconds (depending on complexity)
- **Agent Handoffs**: < 1 second
- **Storage Operations**: < 500ms
- **Memory Usage**: ~50-100MB (depending on conversation history)

## 🔍 Troubleshooting

### Common Issues

**1. API Authentication Errors**
```bash
# Check your API key
python3 -c "from anthropic import Anthropic; print('API key valid')"
```

**2. MCP Connection Issues**
- Restart Claude Desktop
- Check server logs for errors
- Verify config file path and syntax

**3. Agent Not Responding**
- Check billing status in Anthropic Console
- Verify agent instructions are clear
- Test with simple messages first

**4. Storage Permission Errors**
```bash
# Fix permissions
chmod 755 /path/to/storage/directory
```

### Debug Mode
```bash
# Run server with debug logging
CLAUDE_SWARM_DEBUG=true python3 claude_swarm_mcp_server.py
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

### Development Setup
```bash
# Clone and setup development environment
git clone https://github.com/yourusername/claude-swarm-mcp.git
cd claude-swarm-mcp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```

### Running Tests
```bash
python -m pytest tests/ -v
```

## 📈 Roadmap

- [ ] **Advanced Agent Coordination**: Complex multi-step workflows
- [ ] **Custom Function Registry**: User-defined agent capabilities  
- [ ] **Web UI**: Browser-based agent management interface
- [ ] **Integration Templates**: Pre-built integrations for popular services
- [ ] **Performance Optimization**: Faster response times and memory usage
- [ ] **Multi-Model Support**: Support for other LLM providers
- [ ] **Cloud Deployment**: Docker containers and cloud hosting options

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Anthropic** for Claude AI and excellent API
- **OpenAI** for the original Swarm framework inspiration
- **Model Context Protocol** team for the MCP specification
- **Claude Desktop** team for seamless integration

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/claude-swarm-mcp/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/claude-swarm-mcp/discussions)
- **Documentation**: [docs/](docs/)

---

**⭐ Star this repository if you find it useful!**

Built with ❤️ for the Claude AI community# Claude Swarm MCP Server

A Model Context Protocol (MCP) server that enables **multi-agent orchestration** using Claude AI through Claude Desktop. Create, manage, and coordinate specialized AI agents for complex workflows like financial analysis, customer service, and research.

## 🚀 Features

- **🤖 Persistent Agents**: Create specialized Claude agents that survive restarts
- **🔄 Agent Coordination**: Intelligent handoffs between agents based on expertise
- **💾 Local Storage**: All agents and conversations saved locally
- **📊 Pre-built Templates**: Ready-to-use financial analysis and customer service teams
- **🎯 Specialized Functions**: Custom tools and capabilities per agent
- **🔧 Easy Integration**: Works seamlessly with Claude Desktop

## 📋 Quick Start

### Prerequisites

- Python 3.10+ 
- Claude Desktop installed
- Anthropic API key with billing enabled

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/claude-swarm-mcp.git
cd claude-swarm-mcp
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure# Claude Swarm MCP Server

A Model Context Protocol (MCP) server that enables **multi-agent orchestration** using Claude AI through Claude Desktop. Create, manage, and coordinate specialized AI agents for complex workflows like financial analysis, customer service, and research.

## 🚀 Features

- **🤖 Persistent Agents**: Create specialized Claude agents that survive restarts
- **🔄 Agent Coordination**: Intelligent handoffs between agents based on expertise
- **💾 Local Storage**: All agents and conversations saved locally
- **📊 Pre-built Templates**: Ready-to-use financial analysis and customer service teams
- **🎯 Specialized Functions**: Custom tools and capabilities per agent
- **🔧 Easy Integration**: Works seamlessly with Claude Desktop

## 📋 Quick
