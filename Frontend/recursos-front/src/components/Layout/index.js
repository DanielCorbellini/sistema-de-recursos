import Menu from "../Menu";
import Header from "../Header";

const Layout = ({ children }) => {
  return (
    <div className="font-poppins flex h-screen">
      <Menu />
      <div className="flex-1 flex flex-col ml-64">
        {" "}
        {/* Adjust ml-60 based on Menu width */}
        <Header />
        <main className="flex-1 p-6 bg-customGrey text-white">{children}</main>
      </div>
    </div>
  );
};

export default Layout;
