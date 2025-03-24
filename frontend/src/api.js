export async function fetchData() {
    const url = "http://localhost:8000/data";
    try {
        const response = await fetch(url);
        const data = await response.json();

        return data.barplot;
    } catch (error) {
        console.error("ERROR : ", error);
        throw error;
    }
}

//Reemplazar llamadas en BarChart y PieChart por api.js