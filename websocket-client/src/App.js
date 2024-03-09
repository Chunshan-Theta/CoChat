// App.js
import React, {useState, useEffect} from 'react';
import './App.css';
import ChatroomSidebar from './ChatroomSidebar';
import Chatroom from './Chatroom';
import ChatInput from './ChatInput';


const { io } = require("socket.io-client");

const App = () => {
  const [userId, setUserId] = useState(Math.floor(Math.random() * 100000000)); // Example initial room ID
  const [messages, setMessages] = useState([]); // Placeholder for messages
  const socket = io('https://orange-halibut-4j944pxvwphqgq7-8000.app.github.dev');

  const sendMessage = message => {

    // Implement logic to send a message to the current room
    // For example, an API call to send the message to the current room
    // Update the messages state accordingly

    if (message.trim() === "") return;
    

    // Send Socket request to Backend Service
    socket.emit('health-check', {
      text: message,
      name: localStorage.getItem('userName'),
      userId: `${socket.id}${Math.random()}`,
      socketID: socket.id,
    });
  };

  
  useEffect(() => {
    // as soon as the component is mounted, do the following tasks:


    // subscribe to socket events
    socket.on('re-health-check', (msg) => { 
      console.log('Get msg from socket server', msg);
      const newMessage = { id: messages.length + 1, text: msg, sender: 'Me', className_p: "message_user_p", className_span: "message_user_span"}; 
      setMessages(messages => [...messages, newMessage] );
    });

    return () => {
      // before the component is destroyed
      // unbind all event handlers used in this component
      // socket.off("JOIN_REQUEST_ACCEPTED", ()=>{});
    };
  }, [socket, userId,]);
  return (
    <div>
      <div className="forMb">
        <ChatroomSidebar/>
      </div>
      
      <div className="app" userId={userId}>
        <div className="forPc">
          <ChatroomSidebar/>
        </div>
        <div className="main">
          <Chatroom messages={messages} />
          <ChatInput sendMessage={sendMessage} />
        </div>
      </div>
    </div>

  );
};

export default App;
