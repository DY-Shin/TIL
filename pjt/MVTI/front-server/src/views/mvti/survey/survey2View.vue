<template>
  <div>
    <div>
      <img src="@/assets/mvtisurvey/mvti2.jpg" alt="img">
    </div>
    <br>
    <div class="d-grid gap-2 col-6 mx-auto">
      <button class="btn btn-outline-primary" type="button" @click="toGroup1">마동석에게 맞고 이익준에게 치료 받기</button>
      <button class="btn btn-outline-primary" type="button" @click="toGroup2">이익준에게 맞고 마동석에게 수술 받기</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'survey1View',
  methods: {
    toGroup1() {
      this.$store.commit('TOGROUP1')
      this.$router.push({name: 'survey3'})
    },
    toGroup2() {
      this.$store.commit('TOGROUP5')
      this.$router.push({name: 'survey3'})
    }
  }
}
</script>

<style>

</style>