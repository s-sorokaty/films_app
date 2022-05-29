const path = 'http://localhost:8000/'

export const apiPATH = {
    employee: path + 'employee/',
    client: path + 'client/',
    ageRaiting: path + 'age-raiting/',
    filmGenre: path + 'film-genre/',
    filmInfo: path + 'film-info/info/',
    genreOnFilm: path + 'film-info/genre/',
    place: path + 'place/',
    ticketInfo: path + 'ticket-info/'
}

export const apiSecondPATH ={
    coloums: 'coloums'
}

export const apiSelector = [
    {value: 'employee', label: 'Employee', isSearching:false},
    {value: 'client', label: 'Client', isSearching:false},
    {value: 'ageRaiting', label: 'AgeRaiting', isSearching:false},
    {value: 'filmGenre', label: 'FilmGenre', isSearching:false},
    {value: 'filmInfo', label: 'FilmInfo', isSearching:false},
    {value: 'genreOnFilm', label: 'GenreOnFilm', isSearching:false},
    {value: 'place', label: 'Place', isSearching:false},
    {value: 'ticketInfo', label: 'TicketInfo', isSearching:false}
]
export const API = {
    get: async (path, body = undefined) => {
        return fetch(path, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json;charset=utf-8',
            },
        })

    },
    update: async (path, body) => {
        return fetch(path, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
            },
            body:JSON.stringify(body)
        })
    },
    delete: async (path, body) => {
        return fetch(path, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
            },
            body:JSON.stringify(body)
        })

    },
    post: async (path, body) => {
        return fetch(path, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
            },
            body:JSON.stringify(body)
        })

    }
}
