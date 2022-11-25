<template>
  <div>
    <div>
      <img src="@/assets/mvtisurvey/mvti1.jpg" alt="img">
    </div>
    <br>
    <div class="d-grid gap-2 col-6 mx-auto">
      <button class="btn btn-outline-primary" type="button" @click="toGroup1">이상형과 로맨스 주인공</button>
      <button class="btn btn-outline-primary" type="button" @click="toGroup2">초대박 영화 주인공</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'survey1View',
  methods: {
    toGroup1() {
      this.$store.commit('TOGROUP1')
      this.$router.push({name: 'survey2'})
    },
    toGroup2() {
      this.$store.commit('TOGROUP5')
      this.$router.push({name: 'survey2'})
    }
  }
}
</script>

<style>

</style>