Feature: Homepage
    As a visitor,
    when I go to the homepage
    I want to see the lists of post

    Scenario: Create two posts and see their excerpts on homepage
        Given these posts are added
            | title             |
            | Aikidoka talks    |
            | Roles of an Uke   |
        When I visit the homepage
        Then I should see the post "Aikidoka talks"
            And I should see the post "Roles of an Uke"
