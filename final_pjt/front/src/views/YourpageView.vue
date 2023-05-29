<template>
    <div class="container">
      <h1>고마운분, {{ username }} 님</h1>
      <div class="d-flex justify-content-between">
        <div class="d-flex">
          <h3 @click="see_follower">팔로워: {{ followers_count }} | &nbsp;</h3>
          <h3 @click="see_following">팔로잉: {{ followings_count }}</h3>
        </div>
				<div>
          <button class="btn btn-danger" v-if="is_followed" @click="follow">언팔로우</button>
          <button class="btn btn-success" v-else @click="follow">팔로우</button>
        </div>
      </div>
      <div v-if="follower_see & !following_see">
        <hr>
        <h3>팔로워 목록</h3>
        <div v-show="followers.length == 0">
          <img src="@/assets/blank.png" alt="">
        </div>
        <div v-for="(follower, idx) in followers" :key="idx">
          <h4 >
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
          <h4 >
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
      <h3>{{ username }} 님이 선택한 영화들</h3>
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

  const basketURL = "http://127.0.0.1:8000/movies/get_basket/"
  
  export default {
    name: "YourpageView",
    data() {
      return{
        userPK : this.$route.params.pk,
        yourpageURL: "",
        username : "",
        followers: "",
				followers_count : "",
        followings: "",
				followings_count : "",
        baskets: [],
        point : null,
				is_followed : false,
        follower_see : false,
        following_see : false,
      }
    },
  
    computed: {
      JWTToken() {
        return this.$store.state.JWTToken
      },
    },
    methods: {
			follow() {
				axios({
					method : "POST",
					url : "http://localhost:8000/accounts/follow/" + this.userPK + '/',
					headers : {
						Authorization: `Bearer ${this.JWTToken}`
					},
				})
				.then((res) => {
        this.username = res.data.username
        this.followers = res.data.followers
        this.followers_count = this.followers.length
        this.followings = res.data.followings
        this.followings_count = this.followings.length
        this.followings = res.data.followings
				this.is_followed = !this.is_followed
				})
			},
      getUserInfo() {
        axios({
          method: "GET",
          url: this.yourpageURL,
          headers: {
            Authorization: `Bearer ${this.JWTToken}`
          },
      })
      .then((res) => {
        this.username = res.data.username
        this.followers = res.data.followers
        this.followers_count = this.followers.length
        this.followings = res.data.followings
        this.followings_count = this.followings.length
        this.point = res.data.point
				this.followers.forEach((follow) => {
					if (follow.id == this.$store.state.userpk) {
						this.is_followed = true
				}})
      })
      .catch(err=>console.log(err))
      },
      makeURL() {
        this.yourpageURL = "http://localhost:8000/accounts/yourpage/" + this.userPK + "/"
      },
      getBasketInfo() {
        axios({
          method: "GET",
          url: basketURL + this.userPK + '/',
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
      see_follower() {
        this.follower_see = !this.follower_see
        this.following_see = false
      },
      see_following() {
        this.following_see = !this.following_see
        this.follower_see = false
      },
      showImageText(idx) {
        this.baskets[idx].showImageText = true;
      },
      hideImageText(idx) {
        this.baskets[idx].showImageText = false;
      },
      
    },
    mounted() {
      this.makeURL()
      this.getUserInfo()
      this.getBasketInfo()
    }
  }
  </script>
  
  <style>
  /* .carousel-wrapper {
    display: flex;
    align-items: center;
  }
  
  .left-icon-wrapper,
  .right-icon-wrapper {
    flex: 0 0 auto;
  }
  
  .left-icon-wrapper i,
  .right-icon-wrapper i {
    display: flex;
    align-items: center;
    justify-content: center;
    padding-right: 10px;
    padding-left: 10px;
    cursor: pointer;
    transition: background-color 0.3s;
    height: 500px;
    margin-top: -24px;
  }
  
  .carousel {
    flex: 1;
    overflow: hidden;
  }
  
  .carousel-content {
    display: flex;
  }
  
  .carousel .card-img {
    height: 500px;
    object-fit: cover;
    width: 333px;
    cursor: pointer;
    margin-left: 14px;
    border: 0;
  }
  
  .carousel .card-img:nth-of-type(1) {
    margin-left: 0px;
  }
  
  .left-icon-wrapper i:hover,
  .right-icon-wrapper i:hover {
    background-color: rgba(0, 0, 0, 0.2);
  }
  
  .left-icon-wrapper::before,
  .right-icon-wrapper::before {
    content: "";
    display: inline-block;
    vertical-align: middle;
    height: 100%;
  } */
  </style>