<template>
  <div style="  height: 100vh;">
    <div class="mt-4">
      <WatchListForm />
      <WatchListItem />
    </div>
  </div>
</template>

<script>
import WatchListForm from '@/components/WatchListForm.vue';
import WatchListItem from '@/components/WatchListItem.vue';


export default {
  name: 'WatchListView',
  components : {
    WatchListForm,
    WatchListItem
  }
}
</script>

<style>

</style>