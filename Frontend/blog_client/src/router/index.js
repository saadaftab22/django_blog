import { createRouter, createWebHistory } from 'vue-router'
import Login from '../components/Login.vue'
import Blogs from '../components/Blogs.vue'
import Register from '../components/Register.vue'
import Profile from '../components/Profile'
import BlogsFiltered from '../components/BlogsFiltered'
import InvalidPage from '../components/InvalidPage'
import BlogDetail from '../components/BlogDetail'
import EditDeleteBlog from '../components/EditDeleteBlog'
import AddBlog from '../components/AddBlog'
import AddCategory from '../components/AddCategory'
import AdminPanel from '../components/AdminPanel'


const routes = [
 
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {title: 'Login - Blogzilla'},
  },
  {
    path: '/blogs',
    name: 'blogs',
    component: Blogs,
    meta: {title: 'Blogs - Blogzilla'},
  },
  {
    path: '/register',
    name: 'register',
    component: Register,
    meta: {title: 'Register - Blogzilla'},
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: Profile,
    meta: {title: 'Profile - Blogzilla'},
  },
  { 
    path: '/',
    redirect: {name : 'blogs'} 
  },
  {
    path: '/blogs/category/:id',
    name: 'blogs-filtered',
    component: BlogsFiltered,
    meta: {title: 'BlogsF - Blogzilla'},
  },

  {
    path: '/404',
    name: 'invalid-page',
    component: InvalidPage,
    meta: {title: 'Oops - Blogzilla'},

  },

  {
    path: '/blogs/:id',
    name: 'blog-details',
    component: BlogDetail,
    meta: {title: 'BlogPost - Blogzilla'},
  },

  {
    path: '/blogs/edit/:id',
    name: 'blog-edit',
    component: EditDeleteBlog,
    meta: {title: 'Edit Blog - Blogzilla'},
  },

  {
    path: '/blogs/add',
    name: 'blog-add',
    component: AddBlog,
    meta: {title: 'Add Blog - Blogzilla'},
  },

  {
    path: '/categories/add',
    name: 'category-add',
    component: AddCategory,
    meta: {title: 'Add Category - Blogzilla'},
  },

  {
    path: '/admin',
    name: 'admin',
    component: AdminPanel,
    meta: {title: 'Admin Panel - Blogzilla'},
  },
]

const router = createRouter({
  history: createWebHistory(),
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  // This goes through the matched routes from last to first, finding the closest route with a title.
  // e.g., if we have `/some/deep/nested/route` and `/some`, `/deep`, and `/nested` have titles,
  // `/nested`'s will be chosen.
  const nearestWithTitle = to.matched.slice().reverse().find(r => r.meta && r.meta.title);

  // Find the nearest route element with meta tags.
  const nearestWithMeta = to.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);

  const previousNearestWithMeta = from.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);

  // If a route with a title was found, set the document (page) title to that value.
  if(nearestWithTitle) {
    document.title = nearestWithTitle.meta.title;
  } else if(previousNearestWithMeta) {
    document.title = previousNearestWithMeta.meta.title;
  }

  // Remove any stale meta tags from the document using the key attribute we set below.
  Array.from(document.querySelectorAll('[data-vue-router-controlled]')).map(el => el.parentNode.removeChild(el));

  // Skip rendering meta tags if there are none.
  if(!nearestWithMeta) return next();

  // Turn the meta tag definitions into actual elements in the head.
  nearestWithMeta.meta.metaTags.map(tagDef => {
    const tag = document.createElement('meta');

    Object.keys(tagDef).forEach(key => {
      tag.setAttribute(key, tagDef[key]);
    });

    // We use this to track which meta tags we create so we don't interfere with other ones.
    tag.setAttribute('data-vue-router-controlled', '');

    return tag;
  })
  // Add the meta tags to the document head.
  .forEach(tag => document.head.appendChild(tag));

  next();
});

export default router
