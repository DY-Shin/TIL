<template>
  <div>
    <div>
      <img src="@/assets/mvtisurvey/mvti3.jpg" alt="img">
    </div>
    <br>
    <div class="d-grid gap-2 col-6 mx-auto">
      <button class="btn btn-outline-primary" type="button" @click="toGroup1">깊은 숲 속 오두막 혼자가기</button>
      <button class="btn btn-outline-primary" type="button" @click="toGroup2">내가 주최한 30명 단체여행</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'survey1View',
  methods: {
    toGroup1() {
      this.$store.commit('TOGROUP1')
      this.$router.push({name: 'survey4'})
    },
    toGroup2() {
      this.$store.commit('TOGROUP5')
      this.$router.push({name: 'survey4'})
    }
  }
}
</script>

<style>

</style>