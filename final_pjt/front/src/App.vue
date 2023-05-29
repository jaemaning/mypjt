<template>
  <div id="app" :class="{'overflow':mainCheck, 'overflow2':!mainCheck}">
    <MainView v-if="mainCheck"/>
    <div class="container" v-else>
      <div class="nav-box">
        <nav class="d-flex justify-content-between">
          <div class="d-flex" style="cursor: pointer;">
            <img class="mascot" src="./assets/무민.png" alt="" id="moo" @click="toHome" >
            <i class="d-flex" style="margin-top:10px;" @click="toHome"><h3>무비</h3><h5>의</h5><h3>민족</h3></i>
          </div>
          <div>
            <router-link to="/">홈</router-link><span> | </span>
            <router-link v-if="JWTToken" :to="{name:'movies'}">영화</router-link><span v-if="JWTToken"> | </span>
            <router-link v-if="JWTToken" :to="{name:'game'}">게임</router-link><span v-if="JWTToken"> | </span>
            <router-link v-if="!JWTToken" :to="{name:'login'}">로그인</router-link>
            <router-link v-if="JWTToken" :to="{name:'mypage'}">내 정보</router-link><span v-if="JWTToken"> | </span>
            <span v-if="JWTToken" class="logout" @click="logout">로그아웃</span>
          </div>
        </nav>
      </div>
      <router-view/>
    </div>
  </div>
</template>

<script>
import MainView from './components/MainView.vue';

export default {
  name: 'APP',
  data() {
    return {

    }
  },
  components: {
    MainView,
  },
  methods: {
    toHome() {
      if (document.URL === 'http://localhost:8080/') {
        return
      } else {
        this.$router.push({name:'home'})
      }
    },
    logout() {
      this.$store.dispatch('logout')
      if (document.URL === 'http://localhost:8080/') {
        this.$router.go(0);
      } else {
        this.$router.push({name:'home'})
      }
    },
  },
  computed: {
    mainCheck() {
      return this.$store.state.mainCheck
    },
    JWTToken() {
      return this.$store.state.JWTToken ? true : false
    }
  },
  mounted() {
    const bottomElement = document.getElementById('nav-box-id');

    window.addEventListener('scroll', () => {
      const scrollPosition = window.scrollY || window.pageYOffset;
      const windowHeight = window.innerHeight;

      if (scrollPosition + windowHeight >= document.body.offsetHeight) {
        bottomElement.classList.add('show');
      } else {
        bottomElement.classList.remove('show');
      }
    });
  },
  created() {
    document.cookie = 'cross-site-cookie=bar; SameSite=None; Secure';
  }
}
</script>

<style>
/* 기본 글꼴 및 페이지 화면 구성 작성 */
@font-face {
  font-family: "Riders-font";
  src: url("./assets/fonts/BMHANNAPro.ttf");
}
html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
  overflow: auto;
}

#app {
  /* font-family: 'Gowun Dodum', sans-serif; */
  font-family: 'Riders-font';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background-color: rgb(42 193 188);
  height: 100%;
  /* overflow: auto; */
}

/* 이부분 수정 필요 */
.nav-box {
  top: 0px;
  width: 100%;
}

nav {
  padding: 10px 150px 10px;
  line-height: 40px;
  z-index: 2; /* hover-box보다 위에 표시되도록 설정 */
  transition: top 0.5s; /* 애니메이션 전환 속도 */
}

nav a {
  font-weight: bold;
  color: rgb(166 229 227);
  text-decoration: none;
}

/* .hover-box:hover + .nav-box{
  transform: translateY(0); 
} */

nav a.router-link-exact-active {
  color: #2c3e50;
}

.logout {
  font-weight: bold;
  color: rgb(166 229 227);
  text-decoration: none;
  cursor: pointer;
}

.logout:hover {
  color: #0d6efd;
}

.overflow {
  overflow: hidden;
}

.overflow2 {
  overflow: auto;
}

#moo {
  width: 81px;
  height: 54px;

  top: 0px;
  left: 70px;
}

#moo:hover {
  animation: rotate_image 3s linear infinite;transform-origin: 50% 50%;
}

@keyframes rotate_image{
    100% {
        transform: rotate(360deg);
    }
}

.swal12-shown .swal2-height-auto {
  height: 100vh !important;
}


</style>
