textures.py   // Display cart items and total
        System.out.println("Shopping Cart for " + user + ":");
        for (Product product : cart.getItems()) {
            System.out.println(product);
        }
        System.out.println("Total: $" + cart.getTotal());

        // Simulate payment processing
        System.out.print("Enter your credit card number: ");
        String creditCardNumber = scanner.next();

        // Simulate order confirmation
        System.out.println("Order confirmed! We'll send you an email with the details.");

        scanner.close();
    }
}

