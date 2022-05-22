API.get(apiPATH.employee).then(res => {
    return res.json()
})
.then(res => {
    console.log(res)
})

API.get(apiPATH.client).then(res => {
    return res.json()
})
.then(res => {
    console.log(res)
})