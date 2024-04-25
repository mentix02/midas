import useAuthStore from "@/stores/auth";

const useTokenHeader = () => {
  const { token } = useAuthStore();

  return { Authorization: `Token ${token}` };
};

export default useTokenHeader;
