# Recommendation Engine for Midas

Powered by [LightFM](https://making.lyst.com/lightfm/docs/home.html).

Currently we only use the interactions between user.Users & product.Products via heart.Heart relationships
with an implicit weight of 1 but we have plans in the future for incorporating multiple different tyeps of
weighted interactions to build the interaction matrix. For instance -

- a User's past OrderItem's Product could have a weight of 0.75
- a CartItem's Product for a User could have a weight of 0.60
- a (theoretical) View instance of a User could have a weight of 0.25
- and obviously a Heart would directly correspond to a 1.00 (as it does now)
