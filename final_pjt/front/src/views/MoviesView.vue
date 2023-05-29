<template>
  <div class="movies">
    <br>
    <h1>영화 페이지</h1>
    <div >
      <button class="genre-btn" @click="selectAll" :class="{'genre-select': genreSelect[0]}" style="margin:5px; padding:5px;">전체</button>
      <button class="genre-btn" v-for="(genre, id, idx) in movieGenres" :key="id" @click="selectGenre(id, idx+1)" :class="{'genre-select': genreSelect[idx+1]}" style="margin:5px; padding:5px;">{{ genre }}</button>
    </div>
    <br>
    <div v-show="selectGenreMovies.length == 0">
      <img src="@/assets/blank.png" alt="">
    </div>
    <div class="carousel-wrapper" v-show="selectGenreMovies.length != 0">
      <div class="left-icon-wrapper">
        <i class="fa-solid fa-angle-left icon-btn" @click="carouselBtn(false)">왼</i>
      </div>
      <div class="carousel">
        <div class="wrapper">
          <div class="carousel-content">
            <div v-for="(movie, idx) in selectGenreMovies"
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

// const API_KEY = process.env.VUE_APP_TMDB_API_KEY
// const AXIOS_URL = `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko-KR&page=1&sort_by=vote_average.desc&without_genres=99,10755&vote_count.gte=200&api_key=${API_KEY}`

const AXIOS_URL = 'http://localhost:8000/movies/'
const imgURL = 'https://image.tmdb.org/t/p/original'
// const carousel = document.querySelector(".carousel")
// const ifrstImgWidth = carousel.querySelectorAll("img")[0].clientWidth + 14;

export default {
  name: "MoviesView",
  data() {
    return {
      // srcURL : imgURL + this.getMovie.poster_path
      movies : [],
      selectGenreMovies: [],
      movieGenres: {
        '10749' : '로맨스',
        '28' : '액션',
        '27' : '공포',
        '878' : '공상과학',
        '53' : '스릴러',
        '35' : '코미디',
        '12' : '모험',
        '18' : '드라마',
        '16' : '애니메이션',
        '99' : '다큐',
      },
      genreSelect: [
        true,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
      ]
    }
  },
  methods: {
    getMovies () {
      axios({
        method: "GET",
        url: AXIOS_URL
      })
      .then((res)=>{
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
            showImageText: false // showImageText 값 추가 및 초기화
          })
        });
        this.selectGenreMovies = [...this.movies]
      })
      .catch((err)=>{
        console.log(err)
      })
    },
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
    selectGenre(id, idx) {
      const target_idx = this.genreSelect.indexOf(true)
      this.genreSelect.splice(target_idx, 1, false)
      this.genreSelect.splice(idx, 1, true)
      
      this.selectGenreMovies = []
      this.movies.forEach((element)=>{
        const genres = JSON.parse(element.genre_ids)
        if (genres.includes(Number(id))) {
          this.selectGenreMovies.push({
            srcURL: element.srcURL,
            title: element.title,
            vote_average: element.vote_average,
            pk: element.pk,
            showImageText: false // showImageText 값 추가 및 초기화
          })
        }})
      },
    selectAll() {
      const target_idx = this.genreSelect.indexOf(true)
      this.genreSelect.splice(target_idx, 1, false)
      this.genreSelect.splice(0, 1, true)

      this.selectGenreMovies = []
      this.selectGenreMovies = [...this.movies]
    },
    showImageText(idx) {
      this.selectGenreMovies[idx].showImageText = true;
    },
    hideImageText(idx) {
      this.selectGenreMovies[idx].showImageText = false;
    },
  },
  mounted() {
    this.getMovies()
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