<template>
  <div class="container">
    <br>
    <h1>고마운분, {{ username }}(나) 님</h1>
    <div class="d-flex">
      <h3 @click="see_follower">팔로워: {{ followers_count }} |&nbsp;  </h3>
      <h3 @click="see_following">팔로잉: {{ followings_count }}</h3>
    </div>
    <div v-if="follower_see & !following_see">
        <hr>
        <h3>팔로워 목록</h3>
        <div v-show="followers.length == 0">
          <img src="@/assets/blank.png" alt="">
        </div>
        <div v-for="(follower, idx) in followers" :key="idx">
          <h4 @click="toUserInfo(follower)" style="cursor: pointer;">
            {{ follower.username}}
          </h4>
        </div>
      </div>
      <div v-if="following_see & !follower_see">
        <hr>
        <h3>팔로잉 목록</h3>
        <div v-show="followings.length == 0">
          <img src="@/assets/blank.png" alt="">
        </div>
        <div v-for="(following, idx) in followings" :key="idx">
          <h4 @click="toUserInfo(following)" style="cursor: pointer;">
            {{ following.username}}
          </h4>
        </div>
      </div>
    <hr>
    <div class="d-flex justify-content-between">
      <h1>장바구니</h1>
      <h1>포인트 : {{ point }} 점</h1>
    </div>
    <br>
    <h3>내가 선택한 영화들</h3>
    <br>
    <div v-show="baskets.length == 0">
      <img src="@/assets/blank.png" alt="">
    </div>
    <div class="carousel-wrapper" v-show="baskets.length != 0">
      <div class="left-icon-wrapper">
        <i class="fa-solid fa-angle-left icon-btn" @click="carouselBtn(false)">왼</i>
      </div>
      <div class="carousel">
        <div class="wrapper">
          <div class="carousel-content">
            <div v-for="(movie, idx) in baskets"
                :key="idx" class="card-box" :style="{marginLeft:idx==0 ? '0px' : '14px'}">
              <div class="image-wrapper" @mouseenter="showImageText(idx)" @mouseleave="hideImageText(idx)">
                <img
                  class="card-img"
                  :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
                />
                <div class="image-text-container" :class="{ active: movie.showImageText }" @click="toMovieDetail(movie)">
                  <p class="image-text">{{ movie.title }}</p>
                  <div class="d-flex justify-content-center">
                    <i class="material-icons mx-1" style="color: gold">star</i>
                    <p class="image-text">{{ movie.vote_average }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="right-icon-wrapper">
        <i class="fa-solid fa-angle-right icon-btn" @click="carouselBtn(true)">오</i>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

// const URL = "http://localhost:8000/accounts/follow/"
const basketURL = "http://127.0.0.1:8000/movies/get_basket/"


export default {
  name: "MypageView",
  data() {
    return{
      mypageURL: "",
      followers: "",
      followers_count : "",
      followings: "",
      followings_count : "",
      baskets: [],
      follower_see : false,
      following_see : false,
      point : null,
    }
  },
  computed: {
    username (){
      return this.$store.state.username
    },
    JWTToken() {
      return this.$store.state.JWTToken
    },
    userpk() {
      return this.$store.state.userpk
    }
  },
  methods: {
    getUserInfo() {
      axios({
        method: "GET",
        url: this.mypageURL,
        headers: {
          Authorization: `Bearer ${this.JWTToken}`
        },
    })
    .then((res)=>{
      this.followers = res.data.followers
        this.followers_count = this.followers.length
        this.followings = res.data.followings
        this.followings_count = this.followings.length
        this.point = res.data.point
        
    })
    .catch(err=>console.log(err))
    },
    makeURL() {
      this.mypageURL = "http://localhost:8000/accounts/mypage/" + this.$store.state.userpk + "/"
    },
    getBasketInfo() {
      axios({
        method: "GET",
        url: basketURL + this.$store.state.userpk + '/',
        // headers: {
        //   Authorization: `Bearer ${this.JWTToken}`
        // }
      })
      .then((res)=>{
        res.data.forEach(element => {
          element['showImageText'] = false
        });
        this.baskets = res.data
      })
      .catch(err=>console.log(err))
    },
    toMovieDetail(movie) {
      this.$router.push({name:'movie', params: {pk: movie.id}})
    },
    carouselBtn(isRight) {
      const carousel = document.querySelector(".carousel");
      const cardWidth = carousel.querySelector(".card-img").offsetWidth + 7;
      const scrollAmount = isRight ? cardWidth : -cardWidth;

      const currentScrollLeft = carousel.scrollLeft;
      const targetScrollLeft = currentScrollLeft + scrollAmount;

      carousel.scrollTo({
        left: targetScrollLeft,
        behavior: 'smooth'
      });
    },
    showImageText(idx) {
      this.baskets[idx].showImageText = true;
    },
    hideImageText(idx) {
      this.baskets[idx].showImageText = false;
    },
    see_follower() {
      this.follower_see = !this.follower_see
      this.following_see = false
    },
    see_following() {
      this.following_see = !this.following_see
      this.follower_see = false
    },
    toUserInfo(data) {
      this.$router.push({name : 'yourpage', params: {pk:data.id}})
    }
  },
  mounted() {
    this.makeURL()
    this.getUserInfo()
    this.getBasketInfo()
  }
}
</script>

<style>


</style>