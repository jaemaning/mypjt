<template>
  <div>
  <div class="container">
    <br>
    <b-container class="p-5 signup-form w-50">
      <h1>회원가입</h1>
      <br>
      <b-row>
        <label for="id-input">아이디</label>
        <b-form-input 
        id="id-input" 
        v-model="username" 
        :state="usernameState" 
        aria-describedby="input-live-help input-live-feedback" 
        placeholder="아이디를 입력하세요."
        style="font-family: Arial, Helvetica, sans-serif;" 
        trim></b-form-input>
  
        <b-form-invalid-feedback id="id-input-feedback" class="text-right">아이디는 네 글자 이상</b-form-invalid-feedback>
      </b-row>
      <br>
      <b-row>
        <label for="pw-input">비밀번호</label>
        <b-form-input 
        id="pw-input" 
        v-model="password" 
        :state="passwordState" 
        aria-describedby="input-live-help input-live-feedback" 
        placeholder="비밀번호를 입력하세요."
        type="password"
        style="font-family: Arial, Helvetica, sans-serif;" 
        trim></b-form-input>
  
        <b-form-invalid-feedback id="pw-input-feedback" class="text-right">비밀번호는 여덟 글자 이상</b-form-invalid-feedback>
      </b-row>
      <br>
      <b-row>
        <label for="pwconfirm-input">비밀번호 확인</label>
        <b-form-input 
        id="pwconfirm-input" 
        v-model="passwordconfirm" 
        :state="passwordconfirmState" 
        aria-describedby="input-live-help input-live-feedback" 
        placeholder="비밀번호를 입력하세요."
        type="password"
        style="font-family: Arial, Helvetica, sans-serif;" 
        trim></b-form-input>
  
        <b-form-invalid-feedback id="pwconfirm-input-feedback" class="text-right">비밀번호가 일치하지 않습니다.</b-form-invalid-feedback>
      </b-row>
      <br>
      <div class="d-flex justify-content-between">
        <router-link :to="{name:'login'}" class="toLogInA">로그인하러 돌아가기</router-link>
        <b-button @click="signup">회원가입</b-button>
      </div>
      <!-- <br><br><br><br><br><br><br><br><br><br><br><br>/ -->
    </b-container>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import Swal from 'sweetalert2';

const URL = "http://127.0.0.1:8000/auth/signup/"

export default {
  name: "SignupView",
  data() {
    return {
      bodyHeightOn: false,
      username: "",
      password: "",
      passwordconfirm: "",
    }
  },
  computed: {
    usernameState() {
      return this.username.length >= 4 ? true : false
    },
    passwordState() {
      return this.password.length >= 8 ? true : false
    },
    passwordconfirmState() {
      return this.password === this.passwordconfirm && this.passwordconfirm.length >= 8 ? true : false
    }
  },
  methods: {
    showAlertId() {
      Swal.fire({
        title: '아이디가 너무 짧아요!',
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
    showAlertPw1() {
      Swal.fire({
        title: '두 비밀번호가 달라요',
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
    showAlertPw2() {
      Swal.fire({
        title: '비밀번호가 너무 짧아요!',
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
      }),

      document.body.className += 'heightFull'
    },
    showAlertDoubleId() {
      Swal.fire({
        title: '이미 가입된 아이디에요!',
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
        // background: '#fff url("@/assets/1.jpg")',
        // backdrop: `
        //   rgba(0,0,123,0.4)
        //   url("@/assets/1.jpg")
        //   left top
        //   no-repeat
        //   width : "100vh"
        // `
      }),

      document.body.className += 'heightFull'
    },
    signup() {
      if (this.username.length < 4) {
        this.showAlertId()
        return
      }
      
      else if (this.password != this.passwordconfirm) {
        this.showAlertPw1()
        return
      }
      
      else if (this.password.length < 8 || this.passwordconfirm.length < 8) {
        this.showAlertPw2()
        return
      }

      else {
        axios({
          method: "POST",
          url: URL,
          data: {
            username: this.username,
            password1: this.password,
            password2: this.passwordconfirm
          }
        })
        .then((res)=>{
          this.$store.dispatch('signupLogin', res.data)
          this.$router.push({name:"home"})

        })
        .catch(()=>{
          this.showAlertDoubleId()
        })
      }
    }
  }
}
</script>

<style>
.text-right {
  text-align: right;
}

.alert-box {
  position: static;
  background-color: rgba(0, 0, 0, 0.5);
  width: 100vw;
  height: 100vh;
  z-index: 999;
}

.heightFull {
  height: 100vh !important;
}

.custom-modal-content-class {
  width: 300px !important; /* 원하는 너비 값으로 조정 */
  height: 60px !important; /* 원하는 높이 값으로 조정 */
  padding: 2px 0px 0px !important;
  text-align: center;
  /* line-height: 80px !important; */
  font-size: 10px !important;
  color: rgb(241, 129, 129, 1) !important;
  background-color: lightslategray !important;
}

.custom-modal-container-class {
  font-size: 10px;
}

.custom-modal-icon-class{
  transform: scale(0.45) !important;
  margin: 0 !important;
}

.swal2-popup{
  display: flex !important;
  justify-content: center;
}

.custom-modal-title-class {
  padding: 17px 0px 0px !important;
}

.signup-form {
  width: 50%;
  border : 2px solid lightgrey;
  border-radius: 20px;
  background-color: #009996ee;
  box-shadow: 10px 5px 5px lightseagreen;
}

.toLogInA {
  text-decoration: none;
  color: rgb(166 229 227);
}


</style>