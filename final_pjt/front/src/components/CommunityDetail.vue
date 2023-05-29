<template>
  <div>
    <div>
      <h1>커뮤니티</h1>
      <b-row >
        <!-- 별표 보이기 추가 -->
        <div class="d-flex justify-content-center">
        <star-rating v-model="rating"
            :animate="true"
            :active-color="['    #FFE000', '    #FFE000']"
            :active-border-color="['#d8d8d8', '#d8d8d8']"
            :border-width="4"
            :star-points="[
              23, 2, 14, 17, 0, 19, 10, 34, 7, 50, 23, 43, 38, 50, 36, 34, 46,
              19, 31, 17,
            ]"
            :active-on-click="true"
            :clearable="true"
            :star-size="38"
            :increment="1"
          ></star-rating>
        
        <!-- 별표 보이기 추가 -->
        </div>
        <label for="input-username" class="text-left">내용</label>
        <b-form-textarea 
        id="input-username" 
        placeholder="내용" 
        v-model="content" 
        style="font-family: Arial, Helvetica, sans-serif;"
        trim
        ></b-form-textarea>
      </b-row>
      <br>
      <button class="btn" @click="createComment">작성하기</button>
      <br>
      <hr>
    </div>
    <div>
      <h1>커뮤니티 글들</h1>
      <div v-show="communitys.length == 0">
        <img src="@/assets/blank.png" alt="">
      </div>
      <div v-for="(community, idx) in communitys" :key="idx">
        <b-container class="community-box" style="margin-top:10px; margin-bottom:10px;">
          <b-row style="text-align: left; padding: 10px 10px 0px;">
            <!-- <i class="material-icons mx-1" style="color: gold">star</i> -->
            <div class="star-ratings d-flex">
              <div 
                class="star-ratings-fill space-x-2 text-lg"
                :style="{ width: ratingToPercent(community.review) + 'px' }"
              >
                <!-- <span>★dfgh</span><span>★dfgh</span><span>★dfgh</span><span>★dfgh</span><span>★dfgh</span> -->
                <i v-for="index in community.review" :key="index" class="material-icons mx-1" style="-webkit-text-fill-color: gold">star</i>
                <i v-if="!community.review" class="material-icons mx-1" style="-webkit-text-fill-color: white" >star</i>
              </div>
              <div class="star-ratings-base space-x-2 text-lg">
                <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
              </div>
              <b-icon v-if="community.user === loginUser" @click="deleteComment(community.id, idx)" icon="x-square-fill" scale="1" variant="secondary" style="margin-top:8px; margin-left:auto;" class="heart-icon"></b-icon>
            </div>
          </b-row>
          <b-row class="d-flex">
            <b-col class="d-flex content-box">
              <span v-show="community.user === loginUser" class="me">&nbsp;&nbsp;나&nbsp;&nbsp;</span>
              <span v-show="community.user != loginUser" class="me">관람객</span>
              <span class="comm-content"> &nbsp; &nbsp; {{ community.content }} &nbsp;</span> 
              &nbsp;
            </b-col>
          </b-row>
          <b-row>
            <b-col style="text-align:left; padding: 5px 12px 20px;">
              <span><span class="user-btn" @click="toUserInfo(community)">{{ community.username }}</span>&nbsp;|&nbsp;</span> 
              <span><span>{{ community.updated_at.slice(0,4) }}.{{ community.updated_at.slice(5,7) }}.{{ community.updated_at.slice(8,10) }}.&nbsp;{{ community.updated_at.slice(11, 16) }}</span>&nbsp;</span> 
              <!-- <p>영화: {{ community.movie_title }}&nbsp;|&nbsp;</p>  -->
            </b-col>
          </b-row>
          <b-row>
            <div class="d-flex col-12" v-if="!communityLikeList[idx]">
              <b-icon @click="likeComment(community.id, idx)" icon="suit-heart" scale="1" variant="danger" class="heart-icon"></b-icon> &nbsp;&nbsp;<p> {{ community.like_count }}명의 사용자가 이 글을 좋아해요</p>
            </div>
            <div class="d-flex col-12" v-else-if="communityLikeList[idx]">
              <b-icon @click="likeComment(community.id, idx)" icon="suit-heart-fill" scale="1" variant="danger" class="heart-icon"></b-icon> &nbsp;&nbsp;<p> {{ community.like_count }}명의 사용자가 이 글을 좋아해요</p> &nbsp;
            </div>
          </b-row>
        </b-container>
      </div>
    </div>
  </div>
</template>

<script >
import axios from 'axios'
import Swal from 'sweetalert2'
import StarRating from 'vue-star-rating'

	
const commentURL = "http://localhost:8000/movies/" 

export default {
  name: "CommunityDetail",
  props: {
    moviepk: String,
  },
  components : {
      StarRating
    },
  data() {
    return {
      // comment 전용
      user: null,
      content: null,
      communitys: [],
      liked_communitys: [],
      liked_count: null,
      communityLikeList : [],

      // 별표 보이기 추가
      stars: [1, 2, 3, 4, 5],
      selectedStar: null,
      rating : null,
    }
  },
  methods: {
    ratingToPercent(sc) {
      const score = sc * 33;
      return score - 8;
    },
    noContentAlert() {
        Swal.fire({
            title: '내용을 입력하세요!',
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
    noStarAlert() {
        Swal.fire({
            title: '별점을 선택하세요!',
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
    showSuccessAlert() {
      Swal.fire({
        title: '댓글 포인트 +10점',
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
    createComment() {
      if (this.content == null) {
        this.noContentAlert()
        return
      } else if (this.rating == null) {
        this.noStarAlert()
        return
      }
      else {
      axios({
        method: "POST",
        url: commentURL + this.moviepk + "/create_comment/",
        headers: {
          Authorization: `Bearer ${this.JWTToken}`,
          'Content-Type': 'multipart/form-data'
        },
        data: {
          content: this.content,
          review: this.rating,
        }
      })
      .then((res)=>{
        this.communitys = res.data
        this.content = null
        this.communityLikeList.push(false)
        this.showSuccessAlert()
      })
      .catch((err)=>{
        console.log(err)
        alert('로그인을 해주세요.')
      })}
    },
    getComment() {
      axios({
        method: "GET",
        url: commentURL + this.moviepk + "/create_comment/",
        headers: {
          Authorization: `Bearer ${this.JWTToken}`
        },
      })
      .then((res)=>{
        this.communityLikeList = []
        this.communitys = res.data
        res.data.forEach(element => {
          const is_like = element.like_users.includes(this.loginUser) ? true : false
          this.communityLikeList.push(is_like)
        });
      })
      .catch(err=>console.log(err))
    },
    toUserInfo(data){
      if (data.user == this.$store.state.userpk) {
        this.$router.push({name : 'mypage'})
      }
      else {
        this.$router.push({name : 'yourpage', params: {pk:data.user}})
      }
    },
    likeComment(id, idx) {
      axios({
        method : 'POST',
        url : commentURL + this.moviepk + "/like_comment/" + id +"/",
        headers: {
          Authorization: `Bearer ${this.JWTToken}`
        },
      })
      .then((res) => {
        this.communityLikeList.splice(idx, 1, !this.communityLikeList[idx])
        this.communitys[idx].like_count = res.data.like_count
      })
      .catch((err)=> {
        console.log(err)
      })
    },
    deleteComment(id, idx) {
      axios({
        method : 'DELETE',
        url : commentURL + this.moviepk + "/delete_comment/" + id +"/",
        headers: {
          Authorization: `Bearer ${this.JWTToken}`
        },
      })
      .then(() => {
        this.communitys.splice(idx, 1)
        this.communityLikeList.splice(idx, 1)
      })
      .catch((err)=> {
        console.log(err)
      })
    },

    // 별표 보이기 추가
    starClass(starNumber) {
      return {
        filled: starNumber <= this.selectedStar
      };
    },
    hoverStars(starNumber) {
      const stars = document.querySelectorAll('.star_wrap .stars');
      stars.forEach((star, index) => {
        if (index < starNumber) {
          star.classList.add('filled');
        } else {
          star.classList.remove('filled');
        }
      });
    },
    unHoverStars() {
      const stars = document.querySelectorAll('.star_wrap .stars');
      stars.forEach(star => {
        star.classList.remove('filled');
      });
    },
    clickStars(starNumber) {
      const stars = document.querySelectorAll('.star_wrap .stars');
      this.selectedStar = starNumber;
      stars.forEach((star, index) => {
        if (index < starNumber) {
          star.classList.add('filled');
        } else {
          star.classList.remove('filled');
        }
      });
    }
  },
  computed: {
    JWTToken() {
      return this.$store.state.JWTToken
    },
    loginUser() {
      return this.$store.state.userpk
    },
  },
  mounted(){
    this.getComment()
  }
}
</script>

<style>
.me {
  border: 2px solid rgba(204, 76, 76, 0.938);
  border-radius: 8px;
  color: rgba(204, 76, 76, 0.938);
  padding: 2px;
  height: 30px;
}

.comm-content{
  padding: 3px;
  font-size: 22px;
  line-height:20px;
}

.user-btn {
  color: greenyellow;
}
.user-btn:hover {
  cursor: pointer;
}

.heart-icon {
  margin-top: 3px;
  cursor: pointer;
}

.community-box {
  border: 2px solid #eee;
  border-radius: 5px;
  width: 100%;
}

.content-box {
  padding: 10px;
}

#star_div {
   margin: 50px auto;
   width: 300px;
}
.star_wrap {
   padding: 0 10px;
   float: left;
}
.svgf {
   background-color: inherit;
   color: #FDE338;
}

.star-ratings {
  color: white; 
  position: relative;
  unicode-bidi: bidi-override;
  width: max-content;
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 1.3px;
  -webkit-text-stroke-color: gold;
}
 
.star-ratings-fill {
  color: #fff58c;
  padding: 0;
  position: absolute;
  z-index: 1;
  display: flex;
  top: 0;
  left: 0;
  overflow: hidden;
  -webkit-text-fill-color: yellow;
}
 
.star-ratings-base {
  z-index: 0;
  padding: 0;
}
</style>