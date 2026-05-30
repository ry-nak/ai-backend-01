export default async (request) => {
  const url = new URL(request.url);
  const name = url.searchParams.get("name") || "Guest";

  return Response.json({
    message: `Welcome, ${name}! Great to have you here.`
  });
};