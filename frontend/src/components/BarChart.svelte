<script>
  import { onMount } from "svelte";
  import * as echarts from "echarts";

  let chart;
  let chartContainer; // E
  let labels = []; //  eje X
  let values = []; // eje Y

  async function fetchData() {
      const response = await fetch("http://localhost:8000/data");
      const data = await response.json();
      labels = data.barplot.categories;
      values = data.barplot.values;

      drawChart();
    }

  function drawChart() {
    try {
      chart = echarts.init(chartContainer);
      const options = {
        title: {
          text: "Gráfico de Barras",
          left: "center",
        },
        tooltip: {
          trigger: "axis",
        },
        xAxis: {
          type: "category",
          data: labels,
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            type: "bar",
            data: values,
            itemStyle: {
              color: "#de70d2",
            },
          },
        ],
      };

      chart.setOption(options);
    } catch (error) {
      console.error("ERROR EN EL GRAFICO DE BARRAS :", error);
    }
  }

  onMount(fetchData);
</script>

<div
  bind:this={chartContainer}
  style="height: 400px; width: 700%; border: 1px solid #333;"
></div>