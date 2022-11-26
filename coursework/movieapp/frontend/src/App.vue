<template>
  <div class="border rounded bg-info m-4 p-2 text-white">
    <h1>Movie App :)</h1>
  </div>
  <div>
    <button @click="fetch_movies" class="border rounded bg-info h4">Fetch Movies</button>
    <table class="table table-striped mt-4 mb-4">
      <thead class="table-info">
        <tr>
          <th>Movie Title</th>
          <th>Movie ID</th>
          <th>Date Released</th>
          <th>Rating</th>
          <th>Award Winning</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="movie in movies">
          <td>{{ movie.title }}</td>
          <td>{{ movie.id }}</td>
          <td>{{ movie.date_released }}</td>
          <td>{{ movie.rating }}</td>
          <td>{{ movie.award_winning }}</td>
        </tr>
      </tbody>
    </table>
    <AddMovie />
    <DeleteMovie />
    <UpdateMovie />
  </div>
</template>

<script>
import AddMovie from "./components/AddMovie.vue"
import DeleteMovie from "./components/DeleteMovie.vue";
import UpdateMovie from "./components/UpdateMovie.vue";
export default {
    mounted() {
        this.fetch_movies()
    },
    data() {
        return {
            movies: [],
        };
    },
    methods: {
        async fetch_movies() {
            // Perform an Ajax request to fetch the list of movies 
            let response = await fetch("http://127.0.0.1:8000/api/movies/");
            let data = await response.json();
            this.movies = data.movies;
        },
    },
    components: { AddMovie, DeleteMovie, UpdateMovie }
}
</script>


