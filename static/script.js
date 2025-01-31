// document.addEventListener('DOMContentLoaded', function() {
//     // Fetch categories and populate dropdowns
//     fetch('/categories')
//         .then(response => response.json())
//         .then(data => {
//             populateDropdown('region', data.regions);
//             populateDropdown('festival', data.festivals);
//             populateDropdown('tradition', data.traditions);
//         })
//         .catch(error => console.error('Error:', error));

//     // Add event listener to the recommendation button
//     document.querySelector('.recommend-btn').addEventListener('click', getRecommendations);
// });

// function populateDropdown(id, options) {
//     const select = document.getElementById(id);
//     options.forEach(option => {
//         const optionElement = document.createElement('option');
//         optionElement.textContent = option;
//         optionElement.value = option;
//         select.appendChild(optionElement);
//     });
// }

// function getRecommendations() {
//     const region = document.getElementById('region').value;
//     const festival = document.getElementById('festival').value;
//     const tradition = document.getElementById('tradition').value;

//     fetch('/recommend', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({ region, festival, tradition }),
//     })
//     .then(response => response.json())
//     .then(data => displayRecommendations(data))
//     .catch(error => console.error('Error:', error));
// }

// function displayRecommendations(recommendations) {
//     const resultsContainer = document.querySelector('.results');
//     resultsContainer.innerHTML = '';

//     if (recommendations.length === 0) {
//         resultsContainer.innerHTML = '<p class="no-results">No recommendations found. Try different search criteria.</p>';
//         return;
//     }

//     recommendations.forEach(item => {
//         const card = document.createElement('div');
//         card.className = 'music-card';
//         card.innerHTML = `
//             <div class="music-info">
//                 <h3>${item['Song Name']}</h3>
//                 <p class="author">By ${item['Author'] || 'Unknown Artist'}</p>
//                 <div class="tags">
//                     <span class="tag region">${item['Region']}</span>
//                     <span class="tag festival">${item['Festival']}</span>
//                     <span class="tag tradition">${item['Tradition']}</span>
//                 </div>
//                 <a href="${item['URL']}" target="_blank" class="listen-btn">Listen to Song</a>
//             </div>
//         `;
//         resultsContainer.appendChild(card);
//     });
// }