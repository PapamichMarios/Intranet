// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.

export const environment = {
  production: false,
  isMockEnabled: true,
  appVersion: 'intranet-1.0',
  USERDATA_KEY: 'authf649fc9a5f55',

  serverUrl: "http://127.0.0.1:5000/",
  defaultUrl: "/movies",
  
  // auth
  login: "login",
  register: "register",
  profile: "profile",
  change_password: "change_password",

  // admin
  users_all: "/users/all",

  // all
  movies_all: "/movies/all",
  movies_by_id: 'movies/',
  movies_by_name: '/movies/search',
  movies_by_genre: '/movies/all/genre/',
  movie_genres: '/movies/genres'
};

/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/dist/zone-error';  // Included with Angular CLI.
