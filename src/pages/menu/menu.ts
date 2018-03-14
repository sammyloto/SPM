// import { TabsPage } from './../tabs/tabs';
// import { HomePage } from './../home/home';
// import { ContactsPage } from './../contacts/contacts';
// import { ChatsPage } from './../chats/chats';
// import { NotificationsPage } from './../notifications/notifications';
// import { TabsPage } from './../settings/settings';
import { Component, ViewChild } from '@angular/core';
import { IonicPage, NavController, Nav } from 'ionic-angular';
 
export interface PageInterface {
  title: string;
  pageName: string;
  tabComponent?: any;
  index?: number;
  icon: string;
}
 
@IonicPage()
@Component({
  selector: 'page-menu',
  templateUrl: 'menu.html',
})
export class MenuPage {
  // Basic root for our content view
  rootPage = 'HomePage';
 
  // Reference to the app's root nav
  @ViewChild(Nav) nav: Nav;
 
  pages: PageInterface[] = [
    { title: 'Home', pageName: 'HomePage', icon: 'home' },
    { title: 'Profile', pageName: 'ProfilePage', icon: 'person' },
    { title: 'Notifications', pageName: 'NotificationsPage', icon: 'notifications' },
    { title: 'Share', pageName: 'SharePage', icon: 'share' },
    { title: 'Settings', pageName: 'SettingsPage', icon: 'settings' },
    { title: 'Log out', pageName: 'HomePage', icon: 'log-out' }
  ];
 
  constructor(public navCtrl: NavController) { }
 
  openPage(page: PageInterface) {
    let params = {};
 
    // The index is equal to the order of our tabs inside tabs.ts
    if (page.index) {
      params = { tabIndex: page.index };
    }
 
    // The active child nav is our Tabs Navigation
    if (this.nav.getActiveChildNav() && page.index != undefined) {
      this.nav.getActiveChildNav().select(page.index);
    } else {
      // Tabs are not active, so reset the root page 
      // In this case: moving to or from SpecialPage
      this.nav.setRoot(page.pageName, params);
    }
  }
 
  isActive(page: PageInterface) {
    // Again the Tabs Navigation
    let childNav = this.nav.getActiveChildNav();
 
    if (childNav) {
      if (childNav.getSelected() && childNav.getSelected().root === page.tabComponent) {
        return 'primary';
      }
      return;
    }
 
    // Fallback needed when there is no active childnav (tabs not active)
    if (this.nav.getActive() && this.nav.getActive().name === page.pageName) {
      return 'primary';
    }
    return;
  }

  goToLogin() {
    this.navCtrl.setRoot('LoginPage');
  }
 
}