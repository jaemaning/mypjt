<template>
  <div class="top-bgi">
    <div class="background-video">
      <div class="video-wrapper">
        <youtube
          :video-id="video_id"
          :player-vars="playerVars"
          width="100%"
          height="100%"
          @ended="onVideoEnded"
        ></youtube>
      </div>
      <div class="box overlay">
        <!-- 상세 정보 내용 -->
        <!-- <h1>영화 자세히 보기</h1> -->
        <h2>{{ title }}</h2>
        <small>평점 {{ vote_average }}</small>
        <br>
        <small>{{ overview }}</small>
        <br>
      </div>
    </div>
    <br>
    <div class="container">
      <button v-if="haveThisMovie" @click="addMovieToMyBag"><b-icon icon="cart3" scale="1" variant="secondary" class="heart-icon"></b-icon> 장바구니 담기</button>
      <button v-else @click="addMovieToMyBag"><b-icon icon="cart-check-fill" scale="1" variant="secondary" class="heart-icon"></b-icon> 장바구니 빼기</button>
      <br>
      <br>
      <CommunityDetail :moviepk="moviePK"/>
    </div>
</div>
</template>

<script>
import CommunityDetail from '@/components/CommunityDetail.vue';
import axios from 'axios';
import Vue from 'vue'
import VueYoutube from 'vue-youtube'

Vue.use(VueYoutube)

const URL = "http://localhost:8000/movies/"
const basketURL = "http://localhost:8000/movies/basket/"
const commentURL = "http://localhost:8000/movies/" 

export default {
    name: "MovieDetail",
    data() {
        return {
            moviePK: String(this.$route.params.pk),
            backdrop_path: "",
            genre_ids: "",
            overview: "",
            popularity: "",
            poster_path: "",
            release_date: "",
            title: "",
            video: "",
            vote_average: "",
            vote_count: "",
            video_id: "",
            basket_users: [],
        };
    },
    computed: {
        JWTToken() {
            return this.$store.state.JWTToken;
        },
        playerVars() {
            return {
                autoplay: 1,
                mute: 1,
                loop: 1,
                controls: 0,
                modestbranding: 1,
                showinfo: 1,
                rel: 0,
                disablekb: 1,
            };
        },
        haveThisMovie() {
            return this.basket_users.includes(this.$store.state.userpk) ? false : true;
        },
    },
    methods: {
        getDetailMovie() {
            axios({
                method: "GET",
                url: URL + this.moviePK + "/",
                headers: {
                    Authorization: `Bearer ${this.JWTToken}`,
                }
            })
                .then((res) => {
                this.backdrop_path = res.data.backdrop_path;
                this.genre_ids = res.data.genre_ids;
                this.overview = res.data.overview;
                this.popularity = res.data.popularity;
                this.poster_path = res.data.poster_path;
                this.release_date = res.data.release_date;
                this.title = res.data.title;
                this.video = res.data.video;
                this.vote_average = res.data.vote_average;
                this.vote_count = res.data.vote_count;
                this.video_id = res.data.video_id;
                this.basket_users = res.data.basket_users;
            })
                .catch((err) => {
                console.log(err);
            });
        },
        addMovieToMyBag() {
            axios({
                method: "POST",
                url: basketURL + this.moviePK + "/",
                headers: {
                    Authorization: `Bearer ${this.$store.state.JWTToken}`
                },
                data: {
                    user: { pk: this.$store.state.userpk }
                }
            })
                .then((res) => {
                this.basket_users = res.data.basket_users;
                this.haveThisMovie = this.basket_users.includes(this.$store.state.userpk) ? false : true;
            })
                .catch((err) => {
                console.log(err);
            });
        },
        onVideoEnded() {
            const youtubePlayer = this.$refs.youtubePlayer;
            youtubePlayer.playVideo();
        },
        getComment() {
            axios({
                method: "GET",
                url: commentURL + this.moviePK + "/create_comment/",
                headers: {
                    Authorization: `Bearer ${this.JWTToken}`
                },
            })
                .then((res) => {
                this.communitys = res.data;
            })
                .catch(err => console.log(err));
        },
        toUserInfo(data) {
            if (data.user == this.$store.state.userpk) {
                this.$router.push({ name: "mypage" });
            }
            else {
                this.$router.push({ name: "yourpage", params: { pk: data.user } });
            }
        },
        likeComment(idx) {
            axios({
                method: "POST",
                url: commentURL + this.moviePK + "/like_comment/" + (idx + 1) + "/",
                headers: {
                    Authorization: `Bearer ${this.JWTToken}`
                },
            })
                .then(() => {
            })
                .catch((err) => {
                console.log(err);
            });
        },
        ended() {
            this.$refs.player.player.seekTo(0);
        },
    },
    mounted() {
        this.getDetailMovie();
        this.getComment();
    },
    components: { CommunityDetail }
}
</script>

<style>
.background-video {
  position: relative;
  width: 100%;
  height: 0;
  /* 16:9 비율을 위한 값을 설정 (9 / 16 * 100) */
  padding-bottom: 56.25%;
  overflow: hidden;
}

.video-wrapper {
  filter: brightness(0.7);
  position: absolute;
  transform: translate(0%, 0%) scale(1.38);
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.box {
  border: 0;
  margin-top: -90px; /* 배경 동영상의 상단 여백 만큼 밀어 올림 */
  padding-top: 90px; /* 배경 동영상의 상단 여백과 동일한 값을 지정 */
}

.overlay {
  text-align: left;
  position: absolute;
  bottom: 0px;
  margin-bottom: 0px;
  left: 20px;
  width: 60%;
  height: 60%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: left;
  z-index: 1;
  filter: brightness(1);
}

</style>