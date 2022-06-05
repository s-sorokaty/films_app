const path = 'http://localhost:8000/'

export const apiPATH = {
    employee: path + 'employee/',
    client: path + 'client/',
    ageRaiting: path + 'age-raiting/',
    filmGenre: path + 'film-genre/',
    filmInfo: path + 'film-info/info/',
    genreOnFilm: path + 'film-info/genre/',
    place: path + 'place/',
    ticketInfo: path + 'ticket-info/',
    hall: path+ 'hall/'
}

export const apiSecondPATH = {
    coloums: 'coloums'
}

export const selectableColoums = {
    idClient: apiPATH.client,
    idEmployee: apiPATH.employee,
    idPlace: apiPATH.place,
    ageRaiting: apiPATH.ageRaiting,
    idGenre: apiPATH.filmGenre,
    idFilm: apiPATH.filmInfo,
    idHall: apiPATH.hall,
    startTime:'DATE',
    // idHall:apiPATH,
    // idSession:apiPATH,
}

export const apiSelector = [
    { value: 'employee', label: 'Работники', isSearching: false },
    { value: 'client', label: 'Клиенты', isSearching: false },
    { value: 'ageRaiting', label: 'Возврастной рейтинг', isSearching: false },
    { value: 'filmGenre', label: 'Жанры', isSearching: false },
    { value: 'filmInfo', label: 'Информация о фильме', isSearching: false },
    { value: 'genreOnFilm', label: 'Жанры в фильме', isSearching: false },
    { value: 'place', label: 'Места', isSearching: false },
    { value: 'ticketInfo', label: 'Информация о билете', isSearching: false },
    { value: 'hall', label: 'Настройка зала', isSearching: false },
    
]
export const API = {
    get: async (path, body = undefined) => {
        return fetch(path, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json;charset=utf-8',
            },
            body
        }, )

    },
    update: async (path, body) => {
        return fetch(path, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
            },
            body: JSON.stringify(body)
        })
    },
    delete: async (path, body) => {
        return fetch(path, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
            },
            body: JSON.stringify(body)
        })

    },
    post: async (path, body) => {
        return fetch(path, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
            },
            body: JSON.stringify(body)
        })

    }
}
