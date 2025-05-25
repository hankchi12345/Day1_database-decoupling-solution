const express = require('express');
const axios = require('axios');
const app = express();

app.get('/user_full_profile/:userId', async (req, res) => {
  const userId = req.params.userId;

  // 並行請求：User 通用資料 + A 業務個性化資料
  const [userResp, bizResp] = await Promise.all([
    axios.get(`http://user-service.local/user/${userId}`),
    axios.get(`http://bizA-service.local/user-profile/${userId}`)
  ]);

  const fullProfile = {
    ...userResp.data,
    ...bizResp.data
  };

  res.json(fullProfile);
});

app.listen(3000, () => console.log('Aggregate-Service running on port 3000'));
