<template>
  <div class="container">
    <br>
    <h1>게임 페이지</h1>
    <h3 >현재 점수 : {{score}}</h3>
    <h3>남은 기회 : {{count}}</h3>
    <div class="img-div">
      <div class="clipped-image">
        <img class="card-img" :src="poster_path" />
      </div>
    </div>
    <b-row>
        <label for="input-username" class="text-left">제목</label>
        <b-form-input 
        id="input-username" 
        placeholder="내용" 
        v-model="title" 
        style="font-family: Arial, Helvetica, sans-serif;"
        trim
        @keyup.enter="sendAnswer"
        ></b-form-input>
    </b-row>
    <br>
    <button class="btn" @click="bringMovie" v-show="!movie_exists" >문제 불러오기</button>
    <button class="btn" @click="sendAnswer" v-show="movie_exists">답 확인하기</button>
    <button class="btn" @click="clickHint" v-show="movie_exists" >힌트 보기 -100p</button>
    <br>
    <hr>
    <h2 >현재 기록된 점수</h2>
    <div v-for="(scr, idx) in scroe_list" :key="idx" >
      {{scr.user}} : {{scr.score}}
    </div>
  </div>
</template>

<script>
import Swal from 'sweetalert2';
import axios from 'axios';

// 전체가 아닌 일부의 2번 영화 정보에 대한 코멘트로 예시를 들음
const AXIOS_URL = "http://localhost:8000/movies/"
const imgURL = 'https://image.tmdb.org/t/p/original'

export default {
  name: "GameView",
  data() {
    return {
      moviePk : null,
      title: null,
      movie: null,
      communitys : [],
      score: Number(500),
      count : 5,
      poster_path : null,
      movie_exists : false,
      scroe_list : [],
    }
  },
  computed: {
    JWTToken() {
      return this.$store.state.JWTToken
    } 
  },
  components: {
    
  },
  methods: {
    storePoint() {
      axios({
        method: "POST",
        url : "http://localhost:8000/accounts/store_score/",
        headers: {
          Authorization: `Bearer ${this.JWTToken}`,
          
        },
        data : {
          score : this.score / 10
        }
      })
    },
    bringMovie() {
      
      axios({
        method: "GET",
        url: AXIOS_URL + 'bring_movie/',
        headers: {
          Authorization: `Bearer ${this.JWTToken}`,
        },
        
      })
      .then((res)=>{
        this.moviePk = res.data.moviePk
        this.poster_path = imgURL + res.data.poster_path
        this.movie_exists = true
      })
      .catch((err)=>{
        console.log(err)
      })
    
      
    },
    showAlert() {
      Swal.fire({
        title: '답을 입력하세요!',
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
    showxAlert() {
      Swal.fire({
        title: '틀렸습니다! -100점',
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
    showSuccessAlert() {
      Swal.fire({
        title: '정답입니다! +500점',
        icon: 'success',
        position: 'top',
        showConfirmButton: false,
        timer: 2000,
        heightAuto: false, // 높이 자동 조정 비활성화
        customClass: {
          popup: 'custom-modal-content-class-success', // 모달 콘텐츠에 사용자 정의 클래스 추가
          container: 'custom-modal-container-class',
          icon: 'custom-modal-icon-class',
          title: 'custom-modal-title-class'
        },
        padding: '3em',
        color: '#716add',
      })

      document.body.className += 'heightFull'
    },

    sendAnswer() {
      if (this.title === null) {
        this.showAlert()
        return
      } else {
        axios({
          method: "POST",
          url: AXIOS_URL + 'send_answer/' + this.moviePk + '/',
          headers: {
            Authorization: `Bearer ${this.JWTToken}`,
            "Content-Type": "multipart/form-data"
            
          },
          data: {
            answer: this.title
          }
        })
        .then((res)=>{
          this.title = null
          if (res.data.point === 500) {
            this.score += Number(res.data.point)
            this.count = 5
            this.bringMovie()
            this.showSuccessAlert()
          } else {
            this.showxAlert()
            this.score += Number(res.data.point)
            this.count -= 1
            if (this.count === 0) {
              this.scroe_list.push({'user' : this.$store.state.username, 'score': this.score})
              this.storePoint()
              this.count = 5
              this.score = 500
              this.movie_exists = false
              
            }
          }
        })
        .catch(err=>console.log(err))
      }
    },
    clickHint() {
      document.querySelector('.clipped-image').style.transform = `translate(${Math.floor(Math.random() * 100 - 50)}%, ${Math.floor(Math.random() * 100 - 50)}%) scale(2)`
      this.score -= 100
      // document.querySelector('.clipped-image').style.height = '50%'
      // document
    }
  },
  created() {
    this.bringMovie()
  }
}
</script>

<style>
.text-left {
  text-align: left;
}
.img-div {
  width: 333px;
  height: 500px;
  overflow: hidden;
  margin: 0 auto 0;
}

.clipped-image {
  background-size: cover;
  transform: translate(50%, 50%) scale(2);
}

.clipped-image2 {
  width: 100%; /* 포스터의 4분의 1 크기로 조정 */
  height: 50%; /* 포스터의 4분의 1 크기로 조정 */
  overflow: hidden;
}

.custom-modal-content-class-success {
  width: 300px !important; /* 원하는 너비 값으로 조정 */
  height: 60px !important; /* 원하는 높이 값으로 조정 */
  padding: 2px 0px 0px !important;
  text-align: center;
  /* line-height: 80px !important; */
  font-size: 10px !important;
  color: lightgreen !important;
  background-color: lightslategray !important;
}

.card-img {
  width: 200%; /* 포스터 이미지 크기를 2배로 설정 */
  height: 200%; /* 포스터 이미지 크기를 2배로 설정 */
  object-fit: cover;
  object-position: -50% -50%; 
}
.total {
  width : 600px;
  height: 800px;
}

</style>