<script>
  import { onMount } from "svelte";
  import * as echarts from "echarts";

  let chart;

  onMount(async () => {
    try {
      const response = await fetch("http://localhost:8000/data");
      const json = await response.json();

      const option = {
        title: {
          text: "Distribución de Productos",
          left: "center",
        },
        tooltip: {
          trigger: "item",
        },
        series: [
          {
            type: "pie",
            radius: "50%",
            data: json.piechart.labels.map((label, index) => ({
              name: label,
              value: json.piechart.values[index],
            })),
          },
        ],
      };

      chart = echarts.init(document.getElementById("piechart"));
      chart.setOption(option);
    } catch (error) {
      console.error("ERROR: ", error);
    }
  });
</script>

<div id="piechart" style="width: 700px; height: 500px; border: 1px solid #333; border-radius: 1px;">
</div>