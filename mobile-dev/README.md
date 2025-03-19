
# Introduction to Mobile Development with React Native (Expo)

In this guide, we’ll start from scratch and follow a step-by-step approach to learning React Native using **Expo**. Expo simplifies the setup process and speeds up mobile development.

## Step 1: Install Node.js and npm

1. **Search for "How to install Node.js"** on your preferred search engine.
2. Visit the official [Node.js website](https://nodejs.org/) and download the latest LTS version.
3. Install it, ensuring **npm** (Node Package Manager) is included.

### Verification:
```bash
node -v
npm -v
```

## Step 2: Install Expo CLI

1. **Search for "Install Expo CLI"**.
2. Run the following command in your terminal:

    ```bash
    npm install -g expo-cli
    ```

3. Confirm installation with:

    ```bash
    expo --version
    ```

## Step 3: Create a New Expo Project

1. **Search for "Create Expo project"**.
2. Run this command to set up a new project:

    ```bash
    npx create-expo-app MyFirstExpoApp
    cd MyFirstExpoApp
    ```

3. Start the Expo development server:

    ```bash
    npm start
    ```

4. Download the [Expo Go](https://expo.dev/client) app on your mobile device and scan the QR code to preview your app.

## Step 4: Understanding Basic Components

Learn about the core building blocks: `View`, `Text`, `Image`, `Button`, and `TextInput`.

### Example:
```javascript
import React from 'react';
import { View, Text, Button, Alert } from 'react-native';

export default function App() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Hello, Expo!</Text>
      <Button title="Press Me" onPress={() => Alert.alert('Button pressed!')} />
    </View>
  );
}
```

## Step 5: Handling Errors and Reading Stack Traces

Expo provides clear error messages and stack traces to debug your app.

### Example with Error Handling:
```javascript
import React, { useState } from 'react';
import { View, Text, Button } from 'react-native';

export default function App() {
  const [count, setCount] = useState(0);

  const handleError = () => {
    try {
      throw new Error('Simulated error!');
    } catch (error) {
      console.error('Caught error:', error);
      alert(`Error: ${error.message}`);
    }
  };

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Count: {count}</Text>
      <Button title="Increment" onPress={() => setCount(count + 1)} />
      <Button title="Trigger Error" onPress={handleError} />
    </View>
  );
}
```

### How to Read Error Stack Traces:
1. When an error occurs, check the terminal or Expo dev console in your browser.
2. Look for:
   - **Error Message**: Describes the issue (e.g., `undefined is not an object`).
   - **Stack Trace**: Shows the exact line and function where the error occurred.
3. **Search the error message** online to find solutions on platforms like Stack Overflow.

Example error output:
```
Error: Simulated error!
    at handleError (App.js:12:10)
    at onPress (Button.js:45:5)
```

## Step 6: Learn Navigation with Expo Router

Expo supports navigation using **expo-router**.

1. **Search for "Expo router tutorial"**.
2. Install the package:

    ```bash
    npm install expo-router
    ```

3. Set up navigation by following the official [expo-router documentation](https://expo.github.io/router/).

## Step 7: Debugging and Logging

1. Use `console.log()` for general debugging.
2. Access logs using the Expo Developer Tools or by running:

    ```bash
    npx expo start --dev-client
    ```

## Step 8: Build and Share Your Expo App

1. **Search for "Expo build and deploy"**.
2. Build your app using:

    ```bash
    npx expo export
    ```

3. Share your app using Expo Go or publish it to the App Store/Play Store.

---

### Additional Resources:
- [Expo Documentation](https://docs.expo.dev/)
- [React Native Documentation](https://reactnative.dev/)
- [Debugging React Native](https://reactnative.dev/docs/debugging)