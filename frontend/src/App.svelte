<script>
  import PieChart from "./components/PieChart.svelte";
  import BarChart from "./components/BarChart.svelte";
</script>

<main>
  <div class="center-container">
    <PieChart />
  </div>

  <div class="center-container">
    <BarChart />
  </div>

</main>


<style>
  main {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 10px;
  }

  .center-container {
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
