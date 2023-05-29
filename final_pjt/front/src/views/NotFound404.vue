<template>
    <div>
        <h1>404 Not Found</h1>
        <img @click="toHome" src="@/assets/무민2.png" alt="" class="notfoundMoomin">
        <h3>요청하신 페이지를 찾을 수 없습니다.</h3>
        <h4>입력하신 주소가 맞는지 다시 한번 확인해주세요.</h4>
        <button @click="toHome" class="btn" >Home으로 돌아가기</button>
    </div>
</template>

<script>

export default {
    name: 'NotFound404',
    methods: {
        toHome() {
            this.$router.push({name:'home'})
        }
    },
};
</script>

<style scoped>
img {
    width : 600px;
    height: 600px;
}

button{
    font-size: 20px;
    font-weight: bold;
    padding: 20px;
}

.notfoundMoomin {
    cursor: pointer;
}

</style>