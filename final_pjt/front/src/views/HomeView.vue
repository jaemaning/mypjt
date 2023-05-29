<template>
  <div id="home" @click="onClickChange">
    <!-- <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <div v-if="JWTToken">
      <h1>환영합니다! {{ username }} 님!</h1>
      <br>    
      <h1>기분별 장르 추천</h1>
      <div class="img-box d-flex justify-content-center">
        <div class="image-p">
          <img class="home-img-file" src="@/assets/1.jpg" alt="" @click="recommend(0)">
          <p>힘들고 지칠 때</p>
        </div>
        <div class="image-p">
          <img class="home-img-file" src="@/assets/2.jpg" alt="" @click="recommend(3)">
          <p>일상이 지루할 때</p>
        </div>
        <div class="image-p">
          <img class="home-img-file" src="@/assets/3.jpg" alt="" @click="recommend(2)">
          <p>센 척 하고 싶을 때</p>
        </div>
        <div class="image-p">
          <img class="home-img-file" src="@/assets/4.jpg" alt="" @click="recommend(1)">
          <p>연애가 끌릴 때</p>
        </div>
      </div>
      <hr>
      <hr>
      <h1>검색으로 영화 찾기</h1>
      <div class="d-flex flex-column justify-content-center">
        <div>
          <img id="bm-img-1" src="@/assets/배민캐릭터.png" alt="">
        </div>
        <div class="d-flex justify-content-center">
          <input type="text" v-model="inputData" @keyup.enter="search">
          <button @click="search">검색하기</button>
        </div>
      </div>
      <br><br><br>
    </div>
    <div v-else>
      <h1>로그인을 먼저 해주세요.</h1>
    </div>
  </div>
</template>

<script>
export default{
  name: "HomeView",
  data() {
    return {
      inputData : null,
      conditionData : [
        {condition : 'tired', genre_id : [35, 18], speech : '오늘 하루 힘들고 지친 당신에게 무민이 영화 추천해드릴게요.',},
        {condition : 'sweet', genre_id : [10749, 16], speech : '달달한 거 보면서 연애세포를 깨우고 싶다면?',},
        {condition : 'closer', genre_id : [27, 53], speech : '썸녀랑 같이 보면서 더 가까워 지고 싶죠? 걱정 마세요 ^^',},
        {condition : 'bored', genre_id : [878, 12], speech : '일상의 지루함을 달래줄 멋진 모험 가시죠!',}
      ],
    }

  },
  methods: {
    onClickChange() {
      if (this.$store.state.mainCheck) {
        this.warpSpeed = this.warpSpeed > 0 ? 0 : 1;
        setTimeout(() => {
            // this.$router.push({name:"home"})
            this.$store.commit("MainChange")
        }, 5000);
      }
    },
    search() {
      this.$router.push({name:'searchlist', params: {data: this.inputData}})
    },
    recommend(t) {
      this.$router.push({path:`/recommend/${t}`, query: {data: this.conditionData[t].genre_id}})
    }
  },
  computed: {
    JWTToken () {
      return this.$store.state.JWTToken
    },
    username() {
      return this.$store.state.username
    }
  }
}

</script>

<style>
.home-img-file {
  width: 200px;
  height: 200px;
  border-radius: 100px;
  border: 2px solid black;
  margin: 40px;
  cursor: pointer;
}

.home-img-file:hover {
  transform: scale(1.5);
}

img {
  overflow-clip-margin: content-box;
  overflow: clip;
}

.img-box{
  display: block;
  margin-top:auto;
  margin-bottom: 0;
  align-items: right;
}

#bm-img-1{
  width: 600px;
  height: 600px;
}

.ballon-img {
  width: 200px;
  height: 200px;
  /* background-color: azure; */
}

.balloon {
  position: relative;
  display: inline-block;
}

.balloon-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  color: #fff;
  font-size: 18px;
}
.image-p {
  font-size: 30px;
  width: 300px;
}

</style>