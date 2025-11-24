import React, { useState, useRef, useEffect } from "react";
import axios from "axios";
import "./ChatBot.css";

function ChatBot() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const messagesEndRef = useRef(null);

  // Scroll to bottom whenever messages update
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMsg = {
      sender: "You",
      text: input,
      time: new Date().toLocaleTimeString(),
    };
    setMessages((prev) => [...prev, userMsg]);

    try {
      const res = await axios.post("http://127.0.0.1:8000/chat", {
        message: input,
      });

      const botMsg = {
        sender: "Bot",
        text: res.data.reply,
        time: new Date().toLocaleTimeString(),
      };
      setMessages((prev) => [...prev, botMsg]);
    } catch (err) {
      const errorMsg = {
        sender: "Bot",
        text: "Oops! Something went wrong.",
        time: new Date().toLocaleTimeString(),
      };
      setMessages((prev) => [...prev, errorMsg]);
      console.error(err);
    }

    setInput("");
  };

  return (
    <div className="chat-container">
      <div className="chat-header">PCOD Awareness Chatbot 👩‍🦰</div>

      <div className="chat-window">
        {messages.map((m, i) => (
          <div
            key={i}
            className={`chat-message ${
              m.sender === "You" ? "user-msg" : "bot-msg"
            }`}
          >
            <div className="message-text">{m.text}</div>
            <div className="message-time">{m.time}</div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>

      {/* ✅ Disclaimer inside chat, above input */}
      <p className="disclaimer">
        Educational only , not medical advice
      </p>

      <div className="chat-input">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          placeholder="Type a message..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default ChatBot;
