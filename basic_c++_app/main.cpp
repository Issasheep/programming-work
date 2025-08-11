#include <windows.h>

// Function called when events (messages) happen in the window
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    switch (uMsg) {
        case WM_DESTROY: // When the window is closed
            PostQuitMessage(0);
            return 0;
        case WM_COMMAND: // When a button is clicked
            if (LOWORD(wParam) == 1) { // Button ID is 1
                MessageBox(hwnd, "Button Clicked!", "Info", MB_OK);
            }
            break;
    }
    return DefWindowProc(hwnd, uMsg, wParam, lParam);
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE, LPSTR, int nCmdShow) {
    // Define window class
    const char CLASS_NAME[] = "BasicWindowClass";
    WNDCLASS wc = {};
    wc.lpfnWndProc = WindowProc; // Set event handler
    wc.hInstance = hInstance;
    wc.lpszClassName = CLASS_NAME;

    RegisterClass(&wc); // Register window class

    // Create the window
    HWND hwnd = CreateWindowEx(
        0, CLASS_NAME, "Basic C++ UI", // Window class and title
        WS_OVERLAPPEDWINDOW,           // Window style
        CW_USEDEFAULT, CW_USEDEFAULT,  // Position
        400, 200,                      // Size
        NULL, NULL, hInstance, NULL
    );

    // Create a button inside the window
    CreateWindow(
        "BUTTON", "Click Me",          // Button class and text
        WS_TABSTOP | WS_VISIBLE | WS_CHILD | BS_DEFPUSHBUTTON, // Style
        150, 80, 100, 30,              // Position and size
        hwnd, (HMENU)1, hInstance, NULL // Parent window, button ID
    );

    ShowWindow(hwnd, nCmdShow); // Show the window

    // Main message loop (keeps window open and responsive)
    MSG msg = {};
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }
    return 0;
}