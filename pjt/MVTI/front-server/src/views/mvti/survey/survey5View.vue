<template>
  <div>
    <div>
      <img src="@/assets/mvtisurvey/mvti5.jpg" alt="img">
    </div>
    <br>
    <div class="d-grid gap-2 col-6 mx-auto">
      <button class="btn btn-outline-primary" type="button" @click="toGroup3">모든 팀원이 천재 나만 자괴감</button>
      <button class="btn btn-outline-primary" type="button" @click="toGroup4">희망은 나뿐인 팀 소처럼 일하기</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'survey1View',
  methods: {
    toGroup3() {
      this.$store.commit('TOGROUP2')
      this.$router.push({name: 'survey6'})
    }
    ,
    toGroup4() {
      this.$store.commit('TOGROUP6')
      this.$router.push({name: 'survey6'})
    }
  }
}
</script>

<style>

</style>