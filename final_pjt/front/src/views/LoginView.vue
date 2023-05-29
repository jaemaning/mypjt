<template>
  <div class="container">
    <br>
    <b-container role="group" class="p-5 login-form w-50">
      <h1>로그인</h1>
      <br>
      <b-row>
        <label for="input-username">아이디</label>
        <b-form-input 
        id="input-username" 
        placeholder="ID" 
        v-model="username" 
        :state="nameState" 
        aria-describedby="input-live-help input-live-feedback"
        style="font-family: Arial, Helvetica, sans-serif;" 
        @keyup.enter="login"
        trim
        ></b-form-input>

        <b-form-invalid-feedback id="input-username-feedback" class="text-right">아이디 네 글자 이상</b-form-invalid-feedback>
      </b-row>
      <br>
      <b-row>
        <label for="input-password">패스워드</label>
        <b-form-input 
        id="input-password" 
        placeholder="PASSWORD" 
        v-model="password" 
        :state="passwordState" 
        aria-describedby="input-live-help input-live-feedback"
        type="password" 
        style="font-family: Arial, Helvetica, sans-serif;"
        @keyup.enter="login"
        trim
        ></b-form-input>

        <b-form-invalid-feedback id="input-password-feedback" class="text-right">비밀번호 여덟 글자 이상</b-form-invalid-feedback>
      </b-row>
      <br>
      <div class="d-flex justify-content-between">
        <router-link :to="{name:'signup'}">회원가입</router-link>
        <b-button variant="success" style="background-color: green; color: ;" @click="login">로그인</b-button>
      </div>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'
import Swal from 'sweetalert2';

const URL = "http://localhost:8000/auth/login/"

export default {
  name: "LoginView",
  data() {
    return {
      username: "",
      password: "",
    }
  },
  computed: {
    nameState() {
      return this.username.length >= 4 ? true : false
    },
    passwordState() {
      return this.password.length >= 8 ? true : false
    }
  },
  methods: {
    showAlertId() {
      Swal.fire({
        title: '다시 확인하세요!',
        icon: 'error',
        position: 'top',
        showConfirmButton: false,
        timer: 2000,
        heightAuto: false, // 높이 자동 조정 비활성화
        customClass: {
          popup: 'custom-modal-content-class', // 모달 콘텐츠에 사용자 정의 클래스 추가
          container: 'custom-modal-container-class',
          icon: 'custom-modal-icon-class',
          title: 'custom-modal-title-class'
        },
        padding: '3em',
        color: '#716add',
      })

      document.body.className += 'heightFull'
    },
    login(){
      axios({
        method: "POST",
        url: URL,
        data: {
          username: this.username,
          password: this.password
        }
      })
      .then((res)=>{
        this.$store.dispatch('signupLogin', res.data)
        this.$router.push({name:"home"})
      })
      .catch((err)=>{
        console.log(err)
        this.showAlertId()
      })
    }
  }
}
</script>

<style scoped>



a {
  text-decoration: none;
  color: rgb(166 229 227);
}

.login-form {
  width: 50%;
  border : 2px solid lightgrey;
  border-radius: 20px;
  background-color: #009996ee;
  box-shadow: 10px 5px 5px lightseagreen;
}

.cont {
  object-fit: cover;
}

figure {
  display: block;
  /* margin-block-start: 1em;
  margin-block-end: 1em; */
  /* margin-inline-start: 40px;
  margin-inline-end: 40px; */
  width: 95%;
  height: auto;
  left: 0;
  top: 0;
}
.BMimg {
  object-fit: contain;
  /* display: flex; */
  /* float: none; */
  width: 100%;
  height: auto;
  /* right: 0;
  bottom: 0; */
}

.custom-modal-content-class {
  width: 500px !important; /* 원하는 너비 값으로 조정 */
  height: 60px !important; /* 원하는 높이 값으로 조정 */
  padding: 2px 0px 0px !important;
  text-align: center;
  /* line-height: 80px !important; */
  font-size: 10px !important;
  color: rgb(241, 129, 129, 1) !important;
  background-color: #eee !important;
}
/* img {
  overflow-clip-margin: content-box;
  overflow: clip;
} */
</style>