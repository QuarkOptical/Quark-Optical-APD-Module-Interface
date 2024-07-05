
const max_input = document.querySelector("#hv_max");
const max_box = document.getElementById("max_box_value");

const min_input = document.querySelector("#hv_min");
const min_box = document.getElementById("min_box_value");

const t_max_input = document.querySelector("#temp_max");
const t_max_box = document.getElementById("max_temp_box_value")

const t_min_input = document.querySelector("#temp_min");
const t_min_box = document.getElementById("min_temp_box_value")

const hv_input = document.querySelector("#hv_val");
const hv_box = document.getElementById("hv_box_value");


const reading_value = document.querySelector("#reading_value");
const userInput = document.getElementById('user-input');
const terminalOutput = document.getElementById('terminal-output');
const switchElement = document.getElementById("switch");
const clearButton = document.getElementById('clear-button')
const select = document.getElementById('comPorts');
const configureButton = document.getElementById("configure-button");
const refreshButton = document.getElementById('refreshButton')

var checkbox = document.getElementById('advancedSettingsCheckbox');
var advancedSettings = document.getElementById('advancedSettings');
var advancedInputs = advancedSettings.querySelectorAll('input[type="range"]');

min_input.disabled = true;
max_input.disabled = true;
t_max_input.disabled = true;
t_min_input.disabled = true;
hv_input.disabled = true;
checkbox.disabled = true;

let w_voltage_data = 150;
let voltage_data = 0.0;
let temp_data = 0.0;
var seconds = 0;
var time = 0;
let selectedPort;

const electron = require("electron");
const { ipcRenderer } = electron;
const { SerialPort } = require('serialport')


function map(x, in_min, in_max, out_min, out_max) {
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

async function listSerialPorts() {
  select.innerHTML = '';
  const ports = await SerialPort.list();

  ports.sort((a, b) => {
    return a.path.localeCompare(b.path);
  });
  
  ports.forEach(port => {
    const option = document.createElement('option');
    option.value = port.path;
    option.text = port.path;
    select.appendChild(option);
  });
  if (ports.length == 1) {
    selectedPort = ports[0].path;
    switchElement.disabled=false;
  }
  else if(ports.length==0){

    switchElement.disabled=true;
  }
  else {
    switchElement.disabled=false;
    select.addEventListener('change', function () {
      selectedPort = this.value;
    });

  }

}

listSerialPorts()

async function update_v_Data() {
  var label = (time / 10) + 'sn';

  ipcRenderer.send("voltage_chart", "r/CURRENT_HV");
  const receivedVoltageData = await new Promise((resolve) => {
    ipcRenderer.once('received-v-data', (event, receivedData2) => {
      resolve(receivedData2);

    });
  });
  let match2 = receivedVoltageData.match(/=(\d+)/);
  voltage_data = parseFloat(match2[1] / 100).toFixed(2);


  ipcRenderer.send("temp_chart", "r/CURRENT_TEMP");
  const receivedTempData = await new Promise((resolve) => {
    ipcRenderer.once('received-t-data', (event, receivedData) => {
      resolve(receivedData);
    });
  });
  let parts = receivedTempData.split('=');
  temp_data = parseFloat(parts[1] / 100).toFixed(2);


  addData(TempChart, label, temp_data);
  addData(VoltageChart, label, voltage_data);
  time++;
}

function disableAdvanced() {
  advancedInputs.forEach(function (input) {
    input.disabled = true;
  });
  document.documentElement.style.setProperty('--hv-advanced-v-color', '#818181');
  document.documentElement.style.setProperty('--hv-voltage-color', '#096bb2');

}
function enableAdvanced() {
  document.documentElement.style.setProperty('--hv-advanced-v-color', '#096bb2');
  document.documentElement.style.setProperty('--hv-voltage-color', '#818181');
  advancedInputs.forEach(function (input) {
    input.disabled = false;
  });
  hv_box.disable = true;

}

switchElement.addEventListener("change", function () {
  if (this.checked) {
    ipcRenderer.send('selected-port', selectedPort);

    document.documentElement.style.setProperty('--main-color', '#096bb2');
    document.documentElement.style.setProperty('--hv-voltage-color', '#096bb2');

    select.disabled = true;
    checkbox.disabled = false;
    hv_input.disabled = false;
    //Eğer gelişmiş ayarlar checked ise kodu ekle

    // min_input.disabled = false;
    //max_input.disabled = false;
    checkbox.addEventListener('change', function () {
      // Checkbox işaretliyse
      if (checkbox.checked) {

        enableAdvanced();
        hv_input.disabled = true;
      } else {
        disableAdvanced();
        hv_input.disabled = false;
      }
    });

    min_box.addEventListener("input", function () {
      min_input.value = min_box.value;
      min_box.value.textContent = min_box.value;
    })

    min_input.addEventListener("input", (event) => {
      min_box.value = parseFloat(min_input.value).toFixed(2);
      updateValue(event.target.value, min_box);
    });

    updateValue(min_input.value, min_box);

    max_box.addEventListener("input", function () {
      max_input.value = max_box.value;
      max_box.value.textContent = max_box.value;
    })

    max_input.addEventListener("input", (event) => {
      max_box.value = parseFloat(max_input.value).toFixed(2)
      updateValue(event.target.value, max_box);
    });
    updateValue(max_input.value, max_box);

    //temp max
    t_max_box.addEventListener("input", function () {
      t_max_input.value = t_max_box.value;
      t_max_box.value.textContent = t_max_box.value;
    })

    t_max_input.addEventListener("input", (event) => {
      t_max_box.value = parseFloat(t_max_input.value).toFixed(2)
      updateValue(event.target.value, t_max_box);
    });
    updateValue(t_max_input.value, t_max_box);

    //temp min
    t_min_box.addEventListener("input", function () {
      t_min_input.value = t_min_box.value;
      t_min_box.value.textContent = t_min_box.value;
    })

    t_min_input.addEventListener("input", (event) => {
      t_min_box.value = parseFloat(t_min_input.value).toFixed(2)
      updateValue(event.target.value, t_min_box);
    });
    updateValue(t_min_input.value, t_min_box);

    //hv
    hv_box.addEventListener("input", function () {
      hv_input.value = hv_box.value;
      hv_box.value.textContent = hv_box.value;
    })

    hv_input.addEventListener("input", (event) => {
      hv_box.value = parseFloat(hv_input.value).toFixed(2)
      updateValue(event.target.value, hv_box);
    });
    updateValue(hv_input.value, hv_box);



    //--------------------


    updateGauge();

    interval_progress = setInterval(() => {
      updateProgressBar(w_voltage_data, voltage_data);
    }, 100);
    interval_v_chart = setInterval(update_v_Data, 100);
    interval_gauge = setInterval(updateGauge, 100);


  } else {
    ipcRenderer.send("close");
    document.documentElement.style.setProperty('--hv-voltage-color', '#818181');
    document.documentElement.style.setProperty('--hv-advanced-v-color', '#818181');
    document.documentElement.style.setProperty('--main-color', '#818181');


    select.disabled = false;
    min_input.disabled = true;
    max_input.disabled = true;
    t_max_input.disabled = true;
    t_min_input.disabled = true;
    hv_input.disabled = true;
    checkbox.disabled = true;
    clearInterval(interval_v_chart);
    clearInterval(interval_gauge);
    clearInterval(interval_progress);
  }
});

let terminalout = '';

userInput.addEventListener('keydown', function (event) {
  if (!switchElement.checked) { // Switch kontrol edilmediğinde (kapalı olduğunda)
    event.preventDefault(); // Klavye girişini engelle
    return;
  }

  if (event.key === 'Enter') {
    const inputText = userInput.value;
    if (inputText.trim() === "/clear") {
      terminalOutput.innerHTML = ''; // Terminal içeriğini temizle
      userInput.value = ''; // Kullanıcı girişini temizle
      return; // İşlemi sonlandır
    }
    else if (inputText.trim() === "/h" || inputText.trim() === "/help") {
      const helpText =
        `
        /help Commands:<br>
        w/VOLTAGE=(number) - Sets the desired voltage to the specified number.<br>
        w/MODE=(number) - Sets the operating mode to the specified number.<br>
        w/MIN_TEMP=(number) - Sets the minimum temperature threshold to the specified number.<br>
        w/MAX_TEMP=(number) - Sets the maximum temperature threshold to the specified number.<br>
        w/MIN_HV=(number) - Sets the minimum high voltage threshold to the specified number.<br>
        w/MAX_HV=(number) - Sets the maximum high voltage threshold to the specified number.<br>
        w/LED_MODE=(number) - Sets the LED mode to the specified number.<br><br>
        
        r/OUTPUT_VOLTAGE - Displays the output voltage value from the system.<br>
        r/DESIRED_VOLTAGE - Displays the desired voltage value.<br>
        r/MIN_TEMP - Displays the minimum temperature threshold.<br>
        r/MAX_TEMP - Displays the maximum temperature threshold.<br>
        r/MIN_HV - Displays the minimum high voltage threshold.<br>
        r/MAX_HV - Displays the maximum high voltage threshold.<br>
        r/CURRENT_TEMP - Displays the current temperature.<br>
        r/MODE - Displays the operating mode.<br>
        r/STATUS - Displays the system status.<br>
        r/LED_MODE - Displays the LED mode.<br>
        r/MANUFACTURER_ID - Displays the manufacturer ID.<br>
        r/DUMP - Displays system information dump.<br><br>
  
        /clear - Clears the terminal.<br>`;

      terminalOutput.innerHTML = helpText; // Yardım metnini terminalde göster
      userInput.value = ''; // Kullanıcı girişini temizle
      return; // İşlemi sonlandır
    }

    const l = inputText.length;
    //voltage
    if (inputText.startsWith("w/VOLTAGE=")) {
      const temp = inputText.substring(l - 3);
      const temp2 = parseInt(temp);
      if (!isNaN(temp2)) {
        w_voltage_data = temp2;
      }
    }


    else if (inputText.startsWith("w/MIN_TEMP=")) {
      checkbox.checked = true;
      enableAdvanced();
      const temp = inputText.substring(l - 2);
      const temp2 = parseInt(temp);
      t_min_input.value = temp2;
      t_min_box.value = temp2;
    }
    else if (inputText.startsWith("w/MAX_TEMP=")) {
      checkbox.checked = true;
      enableAdvanced();
      const temp = inputText.substring(l - 2);
      const temp2 = parseInt(temp);
      t_max_input.value = temp2;
      t_max_box.value = temp2;
    }
    //Advanced settings
    else if (inputText.startsWith("w/MODE=")) {
      const temp = inputText.substring(l);
      const temp2 = parseInt(temp);
      if (temp2 == 1) {
        disableAdvanced();
        checkbox.checked = false;
      }
      else if (temp2 == 2) {
        enableAdvanced()
        checkbox.checked = false;
      }
    }

    else if (inputText.startsWith("w/MIN_HV=")) {
      checkbox.checked = true;
      enableAdvanced();
      const temp = inputText.substring(l - 3);
      const temp2 = parseInt(temp);
      min_input.value = temp2;
      min_box.value = temp2;


    }
    else if (inputText.startsWith("w/MAX_HV=")) {
      checkbox.checked = true;
      enableAdvanced();
      const temp = inputText.substring(l - 3);
      const temp2 = parseInt(temp);
      max_input.value = temp2;
      max_box.value = temp2;

    }
    else if (inputText.startsWith("w/LED_MODE=")) {
      const temp = inputText.substring(l - 3);
      const temp2 = parseInt(temp);

    }
    else if (inputText.startsWith("SEND_CONFIGURATION")) {
      checkbox.checked = true;
      enableAdvanced();
      configureButton.click();
    }

    userInput.value = '';
    terminalOutput.scrollTop = terminalOutput.scrollHeight;
    ipcRenderer.send("key", inputText);

    ipcRenderer.once('t_received-data', (event, receivedData2) => {
      terminalout = receivedData2;
      terminalOutput.innerHTML += `<div><span class="prompt">></span>${inputText + "\n" + terminalout}</div>`;
    });
  }
});


function updateGauge() {
  const gauge = document.querySelector('.gauge');
  const percentage = gauge.querySelector('.percentage');
  const value = gauge.querySelector('.value');

  let rotation;
  if (temp_data >= -10 && temp_data < 0) {
    rotation = -temp_data * 2.25; // Mavi: -10 ile 10 arası
    gauge.style.setProperty('--main-color', '#1599A0'); // Mavi
  }
  else if (temp_data >= 0 && temp_data < 10) {
    rotation = (temp_data * 2.25) + 22.5;
    gauge.style.setProperty('--main-color', '#1599A0'); // Mavi

  } else if (temp_data >= 10 && temp_data < 30) {
    rotation = (temp_data * 2.25) + 22.5;
    gauge.style.setProperty('--main-color', '#59A015'); // Yeşil

  } else if (temp_data >= 30 && temp_data < 50) {
    rotation = (temp_data * 2.25) + 22.5;
    gauge.style.setProperty('--main-color', '#CFCC1B'); // Sarı

  } else if (temp_data >= 50 && temp_data <= 70) {
    rotation = (temp_data * 2.25) + 22.5;
    gauge.style.setProperty('--main-color', '#A01526');
  }
  percentage.style.setProperty('--rotation', rotation + 'deg');
  value.textContent = temp_data // Değeri güncelle ve noktadan sonra sadece 4 hane göster
}
// İlerleme çubuğunun genişliğini güncelleyen fonksiyon
function updateProgressBar(w_progress, r_progress) {
  updateValue(r_progress, reading_value);

  
  const r_percentage = (r_progress - 100);
  const r_progressBar = document.getElementById("readingProgress");
  r_progressBar.style.width = r_percentage + "%";
}

function updateValue(newValue, outputElement) {
  // Yeni değeri al ve virgülden sonra 2 basamağa yuvarla
  const roundedValue = parseFloat(newValue).toFixed(2);
  // Yeni değeri ekranda göster
  outputElement.textContent = roundedValue;
}

/*Temp Chart*/

var ctx = document.getElementById('TempChart').getContext('2d');
var maxDataLength = 30; // Maksimum 30 veri noktası

var chartData = {
  type:'gauge',
  labels: [],
  datasets: [{
    label: 'Tempature',
    data: [],
    borderColor: '#096bb2',
    borderWidth: 1
  }]
};
var TempChart = new Chart(ctx, {
  type: 'line',
  data: chartData,
  options: {
    responsive: true,
    maintainAspectRatio: false,
    animation: false,
    scales: {
      y: {
        beginAtZero: true,
        suggestedMin: 15, // Minimum değer
        suggestedMax: 40,
      }
    }
  }
});


/*Voltage Chart*/
var ctx = document.getElementById('VoltageChart').getContext('2d');
var maxDataLength = 30; // Maksimum 30 veri noktası
var chartData = {
  labels: [],
  datasets: [{
    label: 'Voltage',
    data: [],
    borderColor: '#096bb2',
    borderWidth: 1
  }]
};
var VoltageChart = new Chart(ctx, {
  type: 'line',
  data: chartData,
  options: {
    responsive: true,
    maintainAspectRatio: false,
    animation: false,
    scales: {
      y: {
        beginAtZero: true,
        suggestedMin: 90, // Minimum değer
        suggestedMax: 220,
      }
    }
  }
});

// Yeni veri eklemek için işlev
function addData(chart, label, data, scale) {
  // Veri noktası eklemeden önce mevcut veri sayısını kontrol et
  if (chart.data.labels.length >= maxDataLength) {
    // Maksimum veri sayısına ulaşıldıysa, eski veri noktalarını kaldır
    var removeCount = chart.data.labels.length - maxDataLength + 1;
    for (var i = 0; i < removeCount; i++) {
      chart.data.labels.shift();
      chart.data.datasets.forEach((dataset) => {
        dataset.data.shift();
      });
    }
  }
  chart.data.labels.push(label);
  chart.data.datasets.forEach((dataset) => {
    dataset.data.push(data);
  });
  chart.update();
}

function map(x, in_min, in_max, out_min, out_max) {
  const result = ((x - in_min) * (out_max - out_min) / (in_max - in_min)) + out_min;

  return result;
}

configureButton.addEventListener("click", async function () {
  clearInterval(interval_v_chart);
  clearInterval(interval_gauge);
  clearInterval(interval_progress);

  if (checkbox.checked) {
      const min_input_value =parseFloat(min_input.value).toFixed(2);
      const max_input_value =parseFloat(max_input.value).toFixed(2);
      const min_temp_value = parseFloat(t_min_input.value).toFixed(2);
      const max_temp_value = parseFloat(t_max_input.value).toFixed(2);
      await new Promise(resolve => setTimeout(resolve, 100)); 

      const commands = [
          "w/DEVICE_MODE=1",
          "w/MIN_TEMP=" + min_temp_value,
          "w/MAX_TEMP=" + max_temp_value,
          "w/MIN_HV=" + min_input_value,
          "w/MAX_HV=" + max_input_value,
      ];

      for (const command of commands) {
        ipcRenderer.send("key", command);
        ipcRenderer.once('t_received-data', (event, receivedData2) => {
          terminalout = receivedData2;
          terminalOutput.innerHTML += `<div><span class="prompt">></span>${command + "\n" + terminalout}</div>`;
        });
          await new Promise(resolve => setTimeout(resolve, 100)); // 100ms delay between commands  
      }
  } else {

      const hv_input_value = parseFloat(hv_input.value).toFixed(2);
      const commands2 = [
        "w/MIN_TEMP=" + 0,
        "w/MAX_TEMP=" + 50,
        "w/MIN_HV=" + 100,
        "w/MAX_HV=" + 200,
    ];

    for (const command of commands2) {
      ipcRenderer.send("key", command);
        await new Promise(resolve => setTimeout(resolve, 10)); // 100ms delay between commands  
    }
    const commands3 = [
      "w/DEVICE_MODE=0",
      "w/CURRENT_HV="+hv_input_value,
  ];

  for (const command of commands3) {
    ipcRenderer.send("key", command);
    ipcRenderer.once('t_received-data', (event, receivedData2) => {
      terminalout = receivedData2;
      terminalOutput.innerHTML += `<div><span class="prompt">></span>${command + "\n" + terminalout}</div>`;
    });
      await new Promise(resolve => setTimeout(resolve, 100)); // 100ms delay between commands  
  }

      w_voltage_data = hv_input_value;

  }

  await new Promise(resolve => setTimeout(resolve, 100)); 
  interval_progress = setInterval(() => {
    updateProgressBar(w_voltage_data, voltage_data);
  }, 100);
  interval_v_chart = setInterval(update_v_Data, 100);
  interval_gauge = setInterval(updateGauge, 100);
});

clearButton.addEventListener('click', function () {
  terminalOutput.innerHTML = '';
  userInput.value = '';
});

refreshButton.addEventListener('click', () => {
  listSerialPorts();
});




// ECharts instance'ı oluştur
var chartDom = document.getElementById('main');
var myChart = echarts.init(chartDom);
var option;

// Grafik için konfigürasyonu belirle
option = {
    title: {
        text: 'ECharts Entry Example'
    },
    tooltip: {},
    legend: {
        data: ['Sales']
    },
    xAxis: {
        data: ['Shirt', 'Cardign', 'Chiffon Shirt', 'Pants', 'Heels', 'Socks']
    },
    yAxis: {},
    series: [{
        name: 'Sales',
        type: 'bar',
        data: [5, 20, 36, 10, 10, 20]
    }]
};

// Konfigürasyonu uygulayarak grafiği çiz
option && myChart.setOption(option);
