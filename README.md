# GitHub User and Repository Analysis

- This project collects data on GitHub users in Sydney with over 100 followers. 
- It also retrieves information about their public repositories, showcasing trends and insights. 
- The analysis provides actionable recommendations for developers to enhance their presence on GitHub.

## Data Collection

To gather data on GitHub users and their repositories, I utilized the GitHub API. The following steps outline the data scraping process:

1. **User Data Retrieval**: I fetched all users in Sydney with over 100 followers using the `GET /search/users` endpoint.
2. **Data Cleaning**: User details, such as company names, were cleaned by trimming whitespace, converting to uppercase, and stripping leading `@` symbols.
3. **Repository Data Retrieval**: For each user, I retrieved up to 500 of their most recently pushed repositories using the `GET /users/{username}/repos` endpoint.

## Interesting Findings

One surprising fact I discovered is that users with a higher number of public repositories tend to have significantly more followers. This correlation suggests that active contributors to the GitHub community often attract more attention and followers.

## Actionable Recommendations

Based on the analysis, I recommend developers increase their contributions by creating and maintaining public repositories. Regular updates and engagement with the community can enhance visibility and potentially lead to more followers and collaboration opportunities.

## Data Files

- **users.csv**: Contains user information for all users in Sydney with over 100 followers.
- **repositories.csv**: Lists the public repositories of these users, along with relevant metrics.

## License

This project is licensed under the MIT License.

