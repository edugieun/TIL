# Vuetify

## Grid System

https://blog.minamiland.com/376

## text alignment

```vue
<h2 class="headline mb-3 text-center text-sm-left">About Me</h2>
```

- `text-center`는 breakpoint 적용이 안되므로, 기본적으로 text-center를 하고 breakpoint는 left나 right에 적용해준다.

## Class 조건문 걸기

- class="text-center [$vuetify.breakpoint.mdAndUp ? 'display-4': 'display-2']"