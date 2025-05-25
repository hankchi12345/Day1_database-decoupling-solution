// clientA.js (Node.js 範例)
const axios = require('axios');

async function getUserData(userId) {
  const res = await axios.get(`http://user-service.local/user/${userId}`);
  console.log("User info from User-Service:", res.data);
}

getUserData("12345");
