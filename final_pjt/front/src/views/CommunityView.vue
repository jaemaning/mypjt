<template>
  <div class="container">
    <br>
    <h1>커뮤니티임</h1>
    <b-row>
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
    <button class="btn" @click="createCommnet">작성하기</button>
    <br>
    <hr>
    <CommunityDetail :communitys="communitys"/>
  </div>
</template>

<script>
import CommunityDetail from '@/components/CommunityDetail.vue';
import axios from 'axios';

// 전체가 아닌 일부의 2번 영화 정보에 대한 코멘트로 예시를 들음
const AXIOS_URL = "http://localhost:8000/movies/3/create_comment/"

export default {
  name: "CommunityView",
  data() {
    return {
      user: null,
      content: null,
      movie: null,
      communitys : [],
    }
  },
  computed: {
    JWTToken() {
      return this.$store.state.JWTToken
    } 
  },
  components: {
    CommunityDetail,
  },
  methods: {
    getComment() {
      axios({
        method: "GET",
        url: AXIOS_URL,
        headers: {
          Authorization: `Bearer ${this.JWTToken}`
        },
      })
      .then((res)=>{
        this.communitys = res.data
      })
      .catch(err=>console.log(err))
    },
  },
  mounted() {
    this.getComment()
  }
}
</script>

<style>
.text-left {
  text-align: left;
}

</style>