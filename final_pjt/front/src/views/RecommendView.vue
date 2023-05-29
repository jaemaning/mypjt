<template>
  <div class="movies">
    <br>
    <h1>이 경우에 이런 영화 어때요?</h1>
    
    <br>
    
    <div class="carousel-wrapper" v-show="movies.length != 0">
      <div class="left-icon-wrapper">
        <i class="fa-solid fa-angle-left icon-btn" @click="carouselBtn(false)">왼</i>
      </div>
      <div class="carousel">
        <div class="wrapper">
          <div class="carousel-content">
            <div v-for="(movie, idx) in movies"
                :key="idx" class="card-box" :style="{marginLeft:idx==0 ? '0px' : '14px'}">
              <div class="image-wrapper" @mouseenter="showImageText(idx)" @mouseleave="hideImageText(idx)">
                <img
                  class="card-img"
                  :src="movie.srcURL"
                />
                <div @click="toMovieDetail(movie)" class="image-text-container" :class="{active: movie.showImageText}">
                  <p class="image-text fs-4">{{ movie.title }}</p>
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
import axios from 'axios'


const imgURL = 'https://image.tmdb.org/t/p/original'

export default {
    name : "RecommendView",
    data() {
        return {
            data : this.$route.query.data,
            movies : [],
        }
    },
    mounted () {
        axios({
          method : "GET",
          url : "http://127.0.0.1:8000/movies/recommend/" + this.data[0] + "/" + this.data[1] + "/",
        })
        .then((res) => {
          res.data.forEach((element) => {
            const srcURL = imgURL + element.poster_path
            const title = element.title
            const vote_average = element.vote_average
            const pk = element.id
            const genre_ids = element.genre_ids

            this.movies.push({
              srcURL: srcURL,
              title: title,
              vote_average: vote_average,
              pk: pk,
              genre_ids: genre_ids,
              showImageText: false
            })
          });
        })
        .catch((err)=> {
            console.log(err)
        })
    },
    methods : {
      toMovieDetail(movie) {
        this.$router.push({name:'movie', params: {pk: movie.pk}})
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
        this.movies[idx].showImageText = true;
      },
      hideImageText(idx) {
        this.movies[idx].showImageText = false;
      },
    }
}
</script>

<style>

.image-wrapper {
  position: relative;
  height: 500px;
}

.genre-btn {
  background-color: darkgrey;
}

.genre-select {
  background-color: #eee;
}

.movies {
  position: relative;
}
.carousel-wrapper {
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
  width: 333px;
  cursor: pointer;
  margin-left: 14px;
  border: 0;
}

.carousel .card-img:nth-of-type(1) {
  margin-left: 0px ; 
}

.image-text-container {
  width: 333px;
  height: 500px;
  transform: translate(0, -100%);
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
  padding-top: 200px;
  visibility: hidden;
  opacity: 0;
  transition: visibility 0s, opacity 0.3s;
  z-index:999;
  cursor: pointer;
}

.image-text-container.active {
  visibility: visible ;
  opacity: 1 ;
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
}

</style>