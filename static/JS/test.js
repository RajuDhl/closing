async function findMismatch(){
    let error = ""
    const formData = new FormData();
    const rc_file = document.getElementById("1c_file").files[0];
    const toga_file = document.getElementById("toga_file").files[0];

    const total_co = document.getElementById("checkouts").value;
    const total_stay = document.getElementById("stayovers").value;
    const dnd = document.getElementById("dnd").value.split(',');
    const nsr = document.getElementById("nsr").value.split(',');
    const b2b = document.getElementById("b2b").value.split(',');
    const nscl = document.getElementById("nscl").value.split(',');
    const clean = document.getElementById("clean").value.split(',');
    const day_use = document.getElementById("day_use").value.split(',');

    formData.append("room_count_file", rc_file)
    formData.append("toga_file", toga_file)
    formData.append("total_co", total_co)
    formData.append("total_stay", total_stay)
    formData.append("dnd", dnd)
    formData.append("nsr", nsr)
    formData.append("b2b", b2b)
    formData.append("nscl", nscl)
    formData.append("clean", clean)
    formData.append("day_use", day_use)

    if (!rc_file || !toga_file){
        if(!rc_file){
            document.getElementById("no_1c_file").innerHTML = "Please select xslx file from 1c";
        }
        if(!toga_file) document.getElementById("no_toga_file").innerHTML = "Please upload toga file";
    }
    else console.log(rc_file)

    await fetch('http://localhost:5000/submit',{
        method: 'POST',
        body: formData
    }).then(async response => {
        if (response.ok) {
            const response_data = await response.json()
            console.log(response_data)
            for(let i=0; i < response_data.length; i++){
                error += response_data[i]
                error += "<br>"
            }
        } else console.error("failed")
    });
    document.getElementById('mismatch').innerHTML = error
}